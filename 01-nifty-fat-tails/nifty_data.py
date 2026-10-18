"""Load daily index closes for the fat-tails notebook.

Nifty 50, best first:
  1. A CSV you download yourself from NSE Indices (niftyindices.com > Reports > Historical Data > NIFTY 50 >
     download), saved next to this file as nifty50.csv. Covers 1990 onwards; the video uses 3 Nov 1995 onwards.
  2. Any CSV path in the NIFTY_CSV environment variable (same columns: a date column and a close column).
  3. Yahoo Finance (^NSEI) through yfinance. No setup, but it only starts in September 2007.
S&P 500: SPX_CSV if set, else Yahoo Finance (^GSPC).
"""
import os
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent


def _read_closes(path) -> pd.Series:
    df = pd.read_csv(path)
    cols = {c.strip().lower(): c for c in df.columns}
    date = next(cols[c] for c in cols if "date" in c)
    close = next(cols[c] for c in cols if c.startswith("close"))
    raw = df[date].astype(str).str.strip()
    if raw.str.match(r"^\d{4}-\d{2}-\d{2}").all():   # ISO dates: never let day-first parsing swap day and month
        when = pd.to_datetime(raw, format="%Y-%m-%d")
    else:                                            # NSE downloads write dates like 03-Nov-1995 or 03 Nov 1995
        when = pd.to_datetime(raw, dayfirst=True, format="mixed")
    s = pd.Series(pd.to_numeric(df[close], errors="coerce").values, index=when, name="close")
    return s.dropna().sort_index()


def _yahoo(ticker, start, end) -> pd.Series:
    import yfinance as yf  # only needed for the fallback
    df = yf.download(ticker, start=start, end=pd.Timestamp(end) + pd.Timedelta(days=1), auto_adjust=False, progress=False)
    s = df["Close"].squeeze().dropna()
    s.name = "close"
    return s


def load_nifty_closes(start="1995-11-03", end="2026-06-30") -> pd.Series:
    for p in [HERE / "nifty50.csv", os.environ.get("NIFTY_CSV")]:
        if p and Path(p).exists():
            s = _read_closes(p)
            print(f"Nifty 50 from {Path(p).name}")
            break
    else:
        s = _yahoo("^NSEI", start, end)
        print("Nifty 50 from Yahoo Finance (starts Sep 2007)")
    return s[start:end]


def load_spx_closes(start="1950-01-01", end="2026-06-30") -> pd.Series:
    p = os.environ.get("SPX_CSV")
    s = _read_closes(p) if p and Path(p).exists() else _yahoo("^GSPC", start, end)
    return s[start:end]


def fit_two_bells(r: pd.Series, iters=500):
    """Zero-mean mixture of two normals fitted by EM: returns (weight of calm bell, sd calm, sd storm)."""
    from scipy import stats
    x = (r - r.mean()).values
    w, s1, s2 = 0.7, x.std() * 0.6, x.std() * 1.8
    for _ in range(iters):
        a = w * stats.norm.pdf(x, 0, s1)
        b = (1 - w) * stats.norm.pdf(x, 0, s2)
        t = a / (a + b)
        w = t.mean()
        s1 = np.sqrt((t * x**2).sum() / t.sum())
        s2 = np.sqrt(((1 - t) * x**2).sum() / (1 - t).sum())
    return float(w), float(s1), float(s2)
