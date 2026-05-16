"""Load ticker symbols and company names for major US indices."""

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


def _wiki_symbol_name_map(
    url: str,
    symbol_columns: tuple[str, ...],
    name_columns: tuple[str, ...] = ("Company", "Security"),
) -> dict[str, str]:
    soup = BeautifulSoup(_get(url), "html.parser")
    for table in soup.select("table.wikitable"):
        headers = [th.get_text(strip=True) for th in table.select("tr th")]
        symbol_index = None
        for name in symbol_columns:
            if name in headers:
                symbol_index = headers.index(name)
                break
        if symbol_index is None:
            continue

        name_index = None
        for name in name_columns:
            if name in headers:
                name_index = headers.index(name)
                break

        result: dict[str, str] = {}
        for row in table.select("tr")[1:]:
            cells = row.select("td")
            if len(cells) <= symbol_index:
                continue
            text = cells[symbol_index].get_text(strip=True)
            symbol = _yahoo_symbol(text)
            if not text or text == "—" or not _is_valid_ticker(symbol):
                continue
            company = symbol
            if name_index is not None and len(cells) > name_index:
                company = cells[name_index].get_text(strip=True) or symbol
            result[symbol] = company
        if result:
            return result
    raise ValueError(f"Could not parse symbol table from {url}")


@lru_cache(maxsize=1)
def sp500_name_map() -> dict[str, str]:
    response = requests.get(
        SP500_CSV_URL,
        headers={"User-Agent": WIKI_USER_AGENT},
        timeout=30,
    )
    response.raise_for_status()
    reader = csv.DictReader(io.StringIO(response.text))
    return {
        _yahoo_symbol(row["Symbol"]): row["Security"]
        for row in reader
        if _is_valid_ticker(_yahoo_symbol(row["Symbol"]))
    }


@lru_cache(maxsize=1)
def dow_name_map() -> dict[str, str]:
    return _wiki_symbol_name_map(
        "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average",
        ("Symbol",),
    )


@lru_cache(maxsize=1)
def nasdaq100_name_map() -> dict[str, str]:
    return _wiki_symbol_name_map(
        "https://en.wikipedia.org/wiki/Nasdaq-100",
        ("Ticker", "Symbol"),
    )


@lru_cache(maxsize=1)
def all_index_names() -> dict[str, str]:
    """Symbol -> company name for S&P 500, Dow 30, and NASDAQ-100."""
    names: dict[str, str] = {}
    names.update(sp500_name_map())
    names.update(dow_name_map())
    names.update(nasdaq100_name_map())
    return names


def all_index_tickers() -> list[str]:
    """Union of S&P 500, Dow 30, and NASDAQ-100 (deduplicated, sorted)."""
    return sorted(all_index_names().keys())
