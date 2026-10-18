# 01 · Fat tails in the Nifty 50

Companion code for The Indic Quant, video 01 (link to follow once published). Every statistic shown in the video
comes from `fat_tails.ipynb`. The notebook is committed with its outputs, so you can read the results without
running anything.

**Education only, not investment advice.**

## What it shows
- Nifty 50 daily returns against the bell curve: 18 days beyond 5σ since 1995, where a bell curve expects 0.004.
- Why: volatility clusters (big moves follow big moves), and a blend of calm and stormy bells has fat tails.
- What's left after adjusting for volatility: jumps, several of them on election-result days.
- Tails thin as days add up into months, but slowly. Tail exponent about 3, like the S&P 500.
- What breaks: a bell-curve 99.9% Value at Risk is breached 7.6× as often as it promises.

## Data
- **Nifty 50:** official daily closes from NSE Indices, 3 Nov 1995 (the index base date) to 30 Jun 2026.
  NSE data isn't redistributed here. To reproduce the video exactly, download it yourself:
  niftyindices.com → Reports → Historical Data → NIFTY 50, then save the CSV as `nifty50.csv` in this folder.
  (`nifty_data.py` reads any CSV with a date column and a close column.)
- **No download?** Run the notebook as it is. It falls back to Yahoo Finance (`^NSEI`), which only starts in Sep 2007.
  Fat tails and volatility clustering are just as clear there. The daily-to-monthly thinning (Ch 6) is not, because
  19 years are dominated by 2008 and 2020.
- **S&P 500:** Yahoo Finance (`^GSPC`), 1950 to 30 Jun 2026.
- Data ends at least three months before publication, in line with SEBI's rules for educational content.

## Run it
```sh
python -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/jupyter lab fat_tails.ipynb
```

## References
- Cont (2001), "Empirical properties of asset returns: stylized facts and statistical issues", *Quantitative Finance* 1(2).
- Pan & Sinha (2008), "Inverse cubic law of index fluctuation distribution in Indian markets", *Physica A* 387.
- Gopikrishnan, Meyer, Amaral & Stanley (1998), "Inverse cubic law for the distribution of stock price variations", *EPJ B* 3.
- Engle (1982), ARCH, *Econometrica* 50(4); Bollerslev (1986), GARCH, *Journal of Econometrics* 31(3).
- Hill (1975), "A simple general approach to inference about the tail of a distribution", *Annals of Statistics* 3(5).
