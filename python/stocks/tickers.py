"""Load ticker symbols for major US indices (S&P 500, Dow 30, NASDAQ-100)."""

from __future__ import annotations

import csv
import io
import re
from functools import lru_cache

import requests
from bs4 import BeautifulSoup

WIKI_USER_AGENT = (
    "Mozilla/5.0 (compatible; Stock52WeekReport/1.0; +https://github.com/)"
)
SP500_CSV_URL = (
    "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/"
    "master/data/constituents.csv"
)


_TICKER_RE = re.compile(r"^[A-Z][A-Z0-9.-]{0,5}$")


def _yahoo_symbol(symbol: str) -> str:
    return symbol.strip().upper().replace(".", "-")


def _is_valid_ticker(symbol: str) -> bool:
    return bool(_TICKER_RE.match(symbol))


def _get(url: str) -> str:
    response = requests.get(
        url,
        headers={"User-Agent": WIKI_USER_AGENT},
        timeout=30,
    )
    response.raise_for_status()
    return response.text


def _wiki_symbols(url: str, column_names: tuple[str, ...]) -> list[str]:
    soup = BeautifulSoup(_get(url), "html.parser")
    for table in soup.select("table.wikitable"):
        headers = [th.get_text(strip=True) for th in table.select("tr th")]
        col_index = None
        for name in column_names:
            if name in headers:
                col_index = headers.index(name)
                break
        if col_index is None:
            continue

        symbols: list[str] = []
        for row in table.select("tr")[1:]:
            cells = row.select("td")
            if len(cells) <= col_index:
                continue
            text = cells[col_index].get_text(strip=True)
            symbol = _yahoo_symbol(text)
            if text and text != "—" and _is_valid_ticker(symbol):
                symbols.append(symbol)
        if symbols:
            return symbols
    raise ValueError(f"Could not parse symbol table from {url}")


@lru_cache(maxsize=1)
def sp500_tickers() -> list[str]:
    response = requests.get(
        SP500_CSV_URL,
        headers={"User-Agent": WIKI_USER_AGENT},
        timeout=30,
    )
    response.raise_for_status()
    reader = csv.DictReader(io.StringIO(response.text))
    return [_yahoo_symbol(row["Symbol"]) for row in reader]


@lru_cache(maxsize=1)
def dow_tickers() -> list[str]:
    return _wiki_symbols(
        "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average",
        ("Symbol",),
    )


@lru_cache(maxsize=1)
def nasdaq100_tickers() -> list[str]:
    return _wiki_symbols(
        "https://en.wikipedia.org/wiki/Nasdaq-100",
        ("Ticker", "Symbol"),
    )


def all_index_tickers() -> list[str]:
    """Union of S&P 500, Dow 30, and NASDAQ-100 (deduplicated, sorted)."""
    combined = set(sp500_tickers()) | set(dow_tickers()) | set(nasdaq100_tickers())
    return sorted(combined)
