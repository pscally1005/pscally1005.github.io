"""Mailing list storage for the 52-week stock report."""

from __future__ import annotations

import json
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path

SUBSCRIBERS_FILE = Path(__file__).resolve().parent / "subscribers.json"
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_subscribers() -> list[dict[str, str]]:
    if not SUBSCRIBERS_FILE.exists():
        return []
    data = json.loads(SUBSCRIBERS_FILE.read_text(encoding="utf-8"))
    return list(data.get("subscribers", []))


def save_subscribers(subscribers: list[dict[str, str]]) -> None:
    payload = {"subscribers": subscribers}
    SUBSCRIBERS_FILE.write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )


def normalize_email(email: str) -> str:
    return email.strip().lower()


def is_valid_email(email: str) -> bool:
    return bool(EMAIL_RE.match(normalize_email(email)))


def find_by_email(subscribers: list[dict[str, str]], email: str) -> dict[str, str] | None:
    target = normalize_email(email)
    for row in subscribers:
        if normalize_email(row["email"]) == target:
            return row
    return None


def find_by_token(subscribers: list[dict[str, str]], token: str) -> dict[str, str] | None:
    token = token.strip()
    for row in subscribers:
        if row.get("token") == token:
            return row
    return None


def subscribe(email: str) -> tuple[str, bool]:
    """Add email. Returns (message, created). created=False if already subscribed."""
    email = normalize_email(email)
    if not is_valid_email(email):
        raise ValueError(f"Invalid email address: {email}")

    subscribers = load_subscribers()
    existing = find_by_email(subscribers, email)
    if existing:
        return (f"{email} is already subscribed.", False)

    subscribers.append(
        {
            "email": email,
            "token": secrets.token_urlsafe(24),
            "subscribed_at": _now_iso(),
        }
    )
    save_subscribers(subscribers)
    return (f"Subscribed {email}.", True)


def unsubscribe_by_token(token: str) -> str:
    subscribers = load_subscribers()
    row = find_by_token(subscribers, token)
    if not row:
        raise ValueError("Invalid or expired unsubscribe link.")

    subscribers = [s for s in subscribers if s.get("token") != token]
    save_subscribers(subscribers)
    return f"Unsubscribed {row['email']}."


def unsubscribe_by_email(email: str) -> str:
    email = normalize_email(email)
    subscribers = load_subscribers()
    row = find_by_email(subscribers, email)
    if not row:
        raise ValueError(f"{email} is not on the mailing list.")

    subscribers = [
        s for s in subscribers if normalize_email(s["email"]) != email
    ]
    save_subscribers(subscribers)
    return f"Unsubscribed {email}."


def active_emails() -> list[dict[str, str]]:
    """Return subscriber rows for sending (email + token)."""
    return load_subscribers()
