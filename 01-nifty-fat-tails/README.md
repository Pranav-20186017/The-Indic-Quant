# 01 · Fat tails in the Nifty 50

This folder holds the code for The Indic Quant, video 01. The link to the video comes after publication.
Every statistic in the video comes from `fat_tails.ipynb`. The notebook is stored with its outputs, so you can
read the results without running it.

**Education only. This is not investment advice.**

## What the notebook shows
- Nifty 50 daily returns, compared with a normal distribution. Since 1995, 18 days are beyond 5σ. A normal distribution expects 0.004.
- The cause: volatility clusters. Big moves follow big moves. A blend of a calm and a stormy normal distribution has fat tails.
- After the volatility adjustment, some jumps remain. Two of them are election-result days.
- Tails get thinner when days add up to months, but slowly. The tail exponent is near 3, as for the S&P 500.
- The cost: a normal 99.9% Value at Risk fails 7.6 times as often as it promises.

## Data
- **Nifty 50:** official daily closes from NSE Indices, from 3 Nov 1995 (the index base date) to 30 Jun 2026.
  This repository does not include NSE data. To get the same numbers as the video, do these steps:
  1. Go to niftyindices.com > Reports > Historical Data > NIFTY 50.
  2. Download the CSV file.
  3. Save it as `nifty50.csv` in this folder.
- **If you do not download the data**, the notebook uses Yahoo Finance (`^NSEI`). That data starts in September 2007.
  Fat tails and volatility clustering show clearly in that window. The daily-to-monthly change (Ch 6) does not,
  because 2008 and 2020 have a large effect on 19 years of data.
- **S&P 500:** Yahoo Finance (`^GSPC`), 1950 to 30 Jun 2026.
- The data ends at least three months before publication. This agrees with the SEBI rules for educational content.

## Run the notebook
```sh
python -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/jupyter lab fat_tails.ipynb
```

## References
- Cont (2001), "Empirical properties of asset returns: stylized facts and statistical issues", *Quantitative Finance* 1(2).
- Pan and Sinha (2008), "Inverse cubic law of index fluctuation distribution in Indian markets", *Physica A* 387.
- Gopikrishnan, Meyer, Amaral and Stanley (1998), "Inverse cubic law for the distribution of stock price variations", *EPJ B* 3.
- Engle (1982), ARCH, *Econometrica* 50(4). Bollerslev (1986), GARCH, *Journal of Econometrics* 31(3).
- Hill (1975), "A simple general approach to inference about the tail of a distribution", *Annals of Statistics* 3(5).
