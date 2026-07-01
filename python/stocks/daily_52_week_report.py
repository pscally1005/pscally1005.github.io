#!/usr/bin/env python3
"""
Scan S&P 500, Dow 30, and NASDAQ-100 stocks for 52-week highs/lows and email a report.

Usage:
  python daily_52_week_report.py              # send email (requires config.env)
  python daily_52_week_report.py --dry-run    # print report to console only
  python daily_52_week_report.py --limit 20   # scan first N tickers (testing)
"""

from __future__ import annotations

import argparse
import os
import re
import smtplib
import sys
from dataclasses import dataclass
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from html import escape
from pathlib import Path
from urllib.parse import urlencode

import yfinance as yf
from dotenv import load_dotenv

from subscribers import active_emails
from tickers import all_index_names, all_index_tickers

SCRIPT_DIR = Path(__file__).resolve().parent
BATCH_SIZE = 40
DEFAULT_FROM = "poormanprotein@gmail.com"


def mailing_api_url() -> str:
    """Apps Script web app URL (same as stocks_mailing_api_url in _config.yml)."""
    env = os.getenv("MAILING_API_URL", "").strip()
    if env:
        return env
    config_path = SCRIPT_DIR.parent.parent / "_config.yml"
    if config_path.exists():
        text = config_path.read_text(encoding="utf-8")
        match = re.search(
            r'^stocks_mailing_api_url:\s*"?([^"\n#]+)"?\s*$',
            text,
            re.MULTILINE,
        )
        if match:
            return match.group(1).strip()
    return ""


def build_unsubscribe_url(token: str) -> str:
    """Direct Apps Script link (same pattern as the subscribe form)."""
    if not token:
        return ""
    api = mailing_api_url().strip()
    if not api:
        return ""
    query = urlencode({"action": "unsubscribe", "token": token})
    if "?" in api:
        return f"{api}&{query}"
    return f"{api}?{query}"


@dataclass
class StockExtreme:
    symbol: str
    name: str
    price: float
    extreme: float
    pct_from_extreme: float


def load_config() -> dict[str, str]:
    env_path = SCRIPT_DIR / "config.env"
    if env_path.exists():
        load_dotenv(env_path)
    else:
        load_dotenv()

    required = ("SMTP_HOST", "SMTP_USER", "SMTP_PASSWORD")
    missing = [key for key in required if not os.getenv(key)]
    if missing:
        raise SystemExit(
            f"Missing config: {', '.join(missing)}. "
            "Set config.env locally or add GitHub repository secrets "
            "(SMTP_HOST, SMTP_USER, SMTP_PASSWORD)."
        )

    return {
        "smtp_host": os.environ["SMTP_HOST"],
        "smtp_port": int(os.getenv("SMTP_PORT") or "587"),
        "smtp_user": os.environ["SMTP_USER"],
        "smtp_password": os.environ["SMTP_PASSWORD"],
        "email_from": (os.getenv("EMAIL_FROM") or DEFAULT_FROM),
        "tolerance_pct": float(os.getenv("TOLERANCE_PCT") or "0.5"),
    }


def get_recipients() -> list[dict[str, str]]:
    subscribers = active_emails()
    if subscribers:
        return subscribers
    fallback = os.getenv("EMAIL_TO", "").strip()
    if fallback:
        return [{"email": fallback, "token": ""}]
    raise SystemExit(
        "No subscribers in subscribers.json. Add emails via /misc/stocks "
        "or set EMAIL_TO for a single-recipient fallback."
    )


def scan_tickers(
    symbols: list[str],
    names: dict[str, str],
    tolerance_pct: float,
) -> tuple[list[StockExtreme], list[StockExtreme], list[str]]:
    """Return (at_high, at_low, failed_symbols)."""
    at_high: list[StockExtreme] = []
    at_low: list[StockExtreme] = []
    failed: list[str] = []

    for start in range(0, len(symbols), BATCH_SIZE):
        batch = symbols[start : start + BATCH_SIZE]
        try:
            raw = yf.download(
                batch,
                period="1y",
                interval="1d",
                group_by="ticker",
                auto_adjust=True,
                progress=False,
                threads=True,
            )
        except Exception:
            failed.extend(batch)
            continue

        if raw.empty:
            failed.extend(batch)
            continue

        multi = len(batch) > 1

        for symbol in batch:
            try:
                if multi:
                    if symbol not in raw.columns.get_level_values(0):
                        failed.append(symbol)
                        continue
                    frame = raw[symbol].dropna(how="all")
                else:
                    frame = raw.dropna(how="all")

                if frame.empty or "Close" not in frame.columns:
                    failed.append(symbol)
                    continue

                closes = frame["Close"].dropna()
                if closes.empty:
                    failed.append(symbol)
                    continue

                price = float(closes.iloc[-1])
                high_52 = float(frame["High"].max())
                low_52 = float(frame["Low"].min())

                if high_52 <= 0 or low_52 <= 0:
                    failed.append(symbol)
                    continue

                high_threshold = high_52 * (1 - tolerance_pct / 100)
                low_threshold = low_52 * (1 + tolerance_pct / 100)

                company = names.get(symbol, symbol)
                if price >= high_threshold:
                    pct = (price / high_52 - 1) * 100
                    at_high.append(
                        StockExtreme(symbol, company, price, high_52, pct)
                    )
                elif price <= low_threshold:
                    pct = (price / low_52 - 1) * 100
                    at_low.append(
                        StockExtreme(symbol, company, price, low_52, pct)
                    )
            except Exception:
                failed.append(symbol)

    at_high.sort(key=lambda s: s.pct_from_extreme, reverse=True)
    at_low.sort(key=lambda s: s.pct_from_extreme)
    return at_high, at_low, failed


def format_table(rows: list[StockExtreme], kind: str) -> str:
    if not rows:
        return f"<p><em>No stocks at 52-week {kind}.</em></p>"

    header = (
        "<tr><th>Symbol</th><th>Company</th><th>Last price</th>"
        f"<th>52-week {kind}</th><th>vs extreme</th></tr>"
    )
    body = []
    for row in rows:
        body.append(
            "<tr>"
            f"<td>{escape(row.symbol)}</td>"
            f"<td>{escape(row.name)}</td>"
            f"<td>${row.price:,.2f}</td>"
            f"<td>${row.extreme:,.2f}</td>"
            f"<td>{row.pct_from_extreme:+.2f}%</td>"
            "</tr>"
        )
    return (
        "<table border='1' cellpadding='6' cellspacing='0' "
        "style='border-collapse:collapse;font-family:sans-serif;font-size:14px'>"
        f"{header}{''.join(body)}</table>"
    )


def unsubscribe_footer_html(unsubscribe_url: str) -> str:
    if not unsubscribe_url:
        return ""
    return (
        '<p style="color:#666;font-size:12px;margin-top:24px">'
        f'<a href="{escape(unsubscribe_url)}">Unsubscribe</a> from this mailing list.'
        "</p>"
    )


def unsubscribe_footer_plain(unsubscribe_url: str) -> str:
    if not unsubscribe_url:
        return ""
    return f"\nUnsubscribe: {unsubscribe_url}\n"


def build_html(
    at_high: list[StockExtreme],
    at_low: list[StockExtreme],
    scanned: int,
    failed: list[str],
    tolerance_pct: float,
    unsubscribe_url: str = "",
) -> str:
    today = date.today().strftime("%A, %B %d, %Y")
    failed_note = ""
    if failed:
        preview = ", ".join(failed[:15])
        extra = f" (+{len(failed) - 15} more)" if len(failed) > 15 else ""
        failed_note = (
            f"<p style='color:#666;font-size:12px'>"
            f"Could not fetch data for {len(failed)} symbols: "
            f"{preview}{extra}</p>"
        )

    return f"""\
<html>
<body style="font-family:sans-serif;color:#222;max-width:900px">
  <h2>52-Week Highs &amp; Lows — {today}</h2>
  <p>
    Scanned <strong>{scanned}</strong> large-cap tickers from the
    S&amp;P 500, Dow Jones Industrial Average, and NASDAQ-100.
    A stock is listed when its last close is within
    <strong>{tolerance_pct:g}%</strong> of its 52-week high or low.
  </p>
  <h3>At 52-week highs ({len(at_high)})</h3>
  {format_table(at_high, "high")}
  <h3>At 52-week lows ({len(at_low)})</h3>
  {format_table(at_low, "low")}
  {failed_note}
  <p style="color:#666;font-size:12px;margin-top:24px">
    Data from Yahoo Finance. Not financial advice.
  </p>
  {unsubscribe_footer_html(unsubscribe_url)}
</body>
</html>"""


def build_plain(
    at_high: list[StockExtreme],
    at_low: list[StockExtreme],
    scanned: int,
    tolerance_pct: float,
    unsubscribe_url: str = "",
) -> str:
    lines = [
        f"52-Week Highs & Lows — {date.today().isoformat()}",
        f"Scanned {scanned} tickers (tolerance {tolerance_pct:g}%).",
        "",
        f"AT 52-WEEK HIGHS ({len(at_high)})",
    ]
    for row in at_high:
        lines.append(
            f"  {row.symbol} ({row.name}): ${row.price:,.2f} "
            f"(high ${row.extreme:,.2f}, {row.pct_from_extreme:+.2f}%)"
        )
    lines.append("")
    lines.append(f"AT 52-WEEK LOWS ({len(at_low)})")
    for row in at_low:
        lines.append(
            f"  {row.symbol} ({row.name}): ${row.price:,.2f} "
            f"(low ${row.extreme:,.2f}, {row.pct_from_extreme:+.2f}%)"
        )
    lines.append(unsubscribe_footer_plain(unsubscribe_url).rstrip())
    return "\n".join(lines).strip() + "\n"


def send_to_subscribers(
    config: dict[str, str],
    subject: str,
    at_high: list[StockExtreme],
    at_low: list[StockExtreme],
    scanned: int,
    failed: list[str],
    tolerance_pct: float,
) -> int:
    recipients = get_recipients()
    sent = 0

    with smtplib.SMTP(config["smtp_host"], config["smtp_port"]) as server:
        server.starttls()
        server.login(config["smtp_user"], config["smtp_password"])

        for row in recipients:
            to_email = row["email"]
            token = row.get("token", "")
            unsub = build_unsubscribe_url(token)
            html = build_html(
                at_high, at_low, scanned, failed, tolerance_pct, unsub
            )
            plain = build_plain(at_high, at_low, scanned, tolerance_pct, unsub)

            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = config["email_from"]
            msg["To"] = to_email
            msg.attach(MIMEText(plain, "plain"))
            msg.attach(MIMEText(html, "html"))
            server.sendmail(config["email_from"], [to_email], msg.as_string())
            sent += 1
            print(f"Sent to {to_email}")

    return sent


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print report to stdout instead of sending email",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Only scan the first N tickers (for quick testing)",
    )
    args = parser.parse_args()

    print("Loading index constituents...")
    names = all_index_names()
    symbols = all_index_tickers()
    if args.limit > 0:
        symbols = symbols[: args.limit]
    print(f"Scanning {len(symbols)} tickers...")

    tolerance = 0.5
    if not args.dry_run:
        config = load_config()
        tolerance = config["tolerance_pct"]
    else:
        tolerance = float(os.getenv("TOLERANCE_PCT", "0.5"))

    at_high, at_low, failed = scan_tickers(symbols, names, tolerance)
    print(
        f"Done: {len(at_high)} at highs, {len(at_low)} at lows, "
        f"{len(failed)} fetch failures."
    )

    subject = (
        f"52-Week Report: {len(at_high)} highs, {len(at_low)} lows "
        f"— {date.today().isoformat()}"
    )

    if args.dry_run:
        sample_unsub = build_unsubscribe_url("example-token") or "(set stocks_mailing_api_url)"
        plain = build_plain(
            at_high, at_low, len(symbols), tolerance, sample_unsub
        )
        print()
        print(plain)
        print(f"Would send to {len(get_recipients())} subscriber(s).")
        return 0

    count = send_to_subscribers(
        config,
        subject,
        at_high,
        at_low,
        len(symbols),
        failed,
        tolerance,
    )
    print(f"Done. Sent {count} email(s) from {config['email_from']}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
