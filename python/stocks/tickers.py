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
    try:
        return _wiki_symbol_name_map(
            "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average",
            ("Symbol",),
        )
    except ValueError:
        # Fallback: return a cached set of known Dow 30 symbols
        return {
            "MMM": "3M",
            "AXP": "American Express",
            "AMGN": "Amgen",
            "AMZN": "Amazon",
            "AAPL": "Apple Inc.",
            "BA": "Boeing",
            "CAT": "Caterpillar Inc.",
            "CVX": "Chevron Corporation",
            "CSCO": "Cisco Systems",
            "KO": "Coca-Cola",
            "DIS": "Walt Disney Company",
            "GS": "Goldman Sachs",
            "HD": "Home Depot",
            "HON": "Honeywell International",
            "IBM": "International Business Machines",
            "JNJ": "Johnson & Johnson",
            "JPM": "JPMorgan Chase",
            "MCD": "McDonald's",
            "MRK": "Merck & Co.",
            "MSFT": "Microsoft Corporation",
            "NKE": "Nike",
            "NVDA": "NVIDIA Corporation",
            "PG": "Procter & Gamble",
            "CRM": "Salesforce",
            "SHW": "Sherwin-Williams",
            "TRV": "Travelers Companies",
            "UNH": "UnitedHealth Group",
            "VZ": "Verizon",
            "V": "Visa",
            "WMT": "Walmart",
        }


@lru_cache(maxsize=1)
def nasdaq100_name_map() -> dict[str, str]:
    try:
        return _wiki_symbol_name_map(
            "https://en.wikipedia.org/wiki/Nasdaq-100",
            ("Ticker", "Symbol"),
        )
    except ValueError:
        # Fallback: use a known set of Nasdaq-100 symbols
        return {
            "AAPL": "Apple Inc.",
            "ABNB": "Airbnb Inc.",
            "ADBE": "Adobe Inc.",
            "ADI": "Analog Devices Inc.",
            "ADP": "Automatic Data Processing Inc.",
            "ADSK": "Autodesk Inc.",
            "AEP": "American Electric Power",
            "ALAB": "Astera Labs Inc.",
            "ALNY": "Alnylam Pharmaceuticals",
            "AMAT": "Applied Materials Inc.",
            "AMD": "Advanced Micro Devices",
            "AMGN": "Amgen Inc.",
            "AMZN": "Amazon.com Inc.",
            "APP": "AppLovin Corporation",
            "ARM": "Arm Holdings plc",
            "ASML": "ASML Holding",
            "AVGO": "Broadcom Inc.",
            "AXON": "Axon Enterprise",
            "BKNG": "Booking Holdings",
            "BKR": "Baker Hughes",
            "CCEP": "Coca-Cola Europacific Partners",
            "CDNS": "Cadence Design Systems",
            "CEG": "Constellation Energy",
            "CMCSA": "Comcast Corporation",
            "COST": "Costco Wholesale",
            "CPRT": "Copart Inc.",
            "CRWD": "CrowdStrike Holdings",
            "CRWV": "CoreWeave Inc.",
            "CSCO": "Cisco Systems",
            "CSX": "CSX Corporation",
            "CTAS": "Cintas Corporation",
            "DASH": "DoorDash",
            "DDOG": "Datadog",
            "DXCM": "DexCom",
            "EXC": "Exelon Corporation",
            "FANG": "Diamondback Energy",
            "FAST": "Fastenal Company",
            "FER": "Ferrovial",
            "FTNT": "Fortinet",
            "GEHC": "GE HealthCare",
            "GILD": "Gilead Sciences",
            "GOOG": "Alphabet Inc.",
            "GOOGL": "Alphabet Inc.",
            "HON": "Honeywell Technologies",
            "IDXX": "IDEXX Laboratories",
            "INTC": "Intel Corporation",
            "INTU": "Intuit Inc.",
            "ISRG": "Intuitive Surgical",
            "KDP": "Keurig Dr Pepper",
            "KHC": "Kraft Heinz",
            "KLAC": "KLA Corporation",
            "LIN": "Linde plc",
            "LITE": "Lumentum Holdings",
            "LRCX": "Lam Research",
            "MAR": "Marriott International",
            "MCHP": "Microchip Technology",
            "MDLZ": "Mondelez International",
            "MELI": "MercadoLibre",
            "META": "Meta Platforms",
            "MNST": "Monster Beverage",
            "MPWR": "Monolithic Power Systems",
            "MRVL": "Marvell Technology",
            "MSFT": "Microsoft Corporation",
            "MSTR": "Strategy Inc.",
            "MU": "Micron Technology",
            "NBIS": "Nebius Group",
            "NFLX": "Netflix Inc.",
            "NVDA": "NVIDIA Corporation",
            "NXPI": "NXP Semiconductors",
            "ODFL": "Old Dominion Freight Line",
            "ORLY": "O'Reilly Automotive",
            "PANW": "Palo Alto Networks",
            "PAYX": "Paychex",
            "PCAR": "PACCAR Inc.",
            "PDD": "PDD Holdings",
            "PEP": "PepsiCo",
            "PLTR": "Palantir Technologies",
            "PYPL": "PayPal Holdings",
            "QCOM": "Qualcomm",
            "REGN": "Regeneron Pharmaceuticals",
            "RKLB": "Rocket Lab",
            "ROP": "Roper Technologies",
            "ROST": "Ross Stores",
            "SBUX": "Starbucks",
            "SHOP": "Shopify",
            "SNDK": "SanDisk",
            "SNPS": "Synopsys",
            "SPCX": "Space Exploration Technologies",
            "STX": "Seagate Technology",
            "TER": "Teradyne",
            "TMUS": "T-Mobile US",
            "TRI": "Thomson Reuters",
            "TSLA": "Tesla Inc.",
            "TTWO": "Take-Two Interactive Software",
            "TXN": "Texas Instruments",
            "VRTX": "Vertex Pharmaceuticals",
            "WBD": "Warner Bros. Discovery",
            "WDAY": "Workday",
            "WDC": "Western Digital",
            "WMT": "Walmart",
            "XEL": "Xcel Energy",
        }


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
