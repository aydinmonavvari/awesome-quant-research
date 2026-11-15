# Awesome Quant Research

[![CI: links & structure](https://github.com/aydinmonavvari/awesome-quant-research/actions/workflows/link-check.yml/badge.svg)](https://github.com/aydinmonavvari/awesome-quant-research/actions/workflows/link-check.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A curated, honestly annotated list of papers, datasets, tools and libraries for quantitative finance research.

## Contents

- [Why this list](#why-this-list) — motivation and selection principles.
- [How annotations work](#how-annotations-work) — what the one-liners do and do not claim.
- [Foundational books & papers](#foundational-books--papers) — the validation-rigor canon: backtest overfitting, multiple testing, leakage-aware cross-validation.
- [Backtesting & validation libraries](#backtesting--validation-libraries) — code for honest simulation and evaluation.
- [Risk & portfolio optimization](#risk--portfolio-optimization) — construction and risk-measurement libraries.
- [Time-series ML & statistics](#time-series-ml--statistics) — general-purpose toolkits heavily used in financial research.
- [Market data & datasets](#market-data--datasets) — free and subscription data sources.
- [Financial NLP](#financial-nlp) — language models and dictionaries for financial text.
- [Community & learning](#community--learning) — Q&A, preprint feeds and broader lists.
- [Companion research repos](#companion-research-repos) — the author's own related repositories.
- [Contributing](#contributing) — how to propose additions.
- [License](#license) — MIT.

## Why this list

Most "AI for trading" content online is written to sell something. This list is the opposite: a small, working collection of what is actually useful when doing quantitative finance and financial-ML research, with an emphasis on validation rigor — backtest overfitting, multiple-testing corrections, leakage-aware cross-validation, and calibration.

What to expect from it:

- Every entry carries a one-line factual annotation; paywalls, commercial status and maintenance state are stated, not hidden.
- Every link was verified at commit time (2026-11) and is re-checked monthly in CI.
- Quality over quantity: entries are added because they are genuinely useful for research, not to pad categories.

Maintained by Aydin Monavvari as part of an open research portfolio — see [Companion research repos](#companion-research-repos).

## How annotations work

- Each entry is a bullet whose title is a link, followed by an em-dash and one factual sentence; a second sentence or a `(Note: ...)` flag follows where relevant.
- Notes about paywalls, commercial licensing or maintenance state are made only when that status was verified at edit time — no star counts, no performance claims, no marketing language.
- Some publisher sites and platforms block automated requests. Where the CI checker cannot see them, they are excluded from automated checking and verified manually at commit time; the exact policy is described in [Contributing](#contributing).

## Foundational books & papers

- [López de Prado (2018), *Advances in Financial Machine Learning*](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086) — the reference book on ML for trading: labeling, sample weights, purged k-fold cross-validation, meta-labeling and backtesting hygiene. (Note: publisher paywall; Wiley's site blocks automated checkers, ISBN cross-checked via Open Library.)
- [Bailey, Borwein, López de Prado & Zhu (2014), "Pseudo-Mathematics and Financial Charlatanism"](https://www.davidhbailey.com/dhbpapers/backtest-pseudo.pdf) — Notices of the AMS article showing how repeated backtesting inflates out-of-sample performance claims; author-hosted preprint PDF.
- [Bailey & López de Prado (2014), "The Deflated Sharpe Ratio"](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf) — corrects the Sharpe ratio for selection bias, multiple testing and non-normal returns; Journal of Portfolio Management 40(5), 94–107; author-hosted PDF.
- [Harvey & Liu (2015), "Backtesting"](https://people.duke.edu/~charvey/Research/Published_Papers/P120_Backtesting.PDF) — how large a holdout sample should be, and why it should be used once; Journal of Portfolio Management 42(1), 13–28; author-hosted PDF.
- [Harvey, Liu & Zhu (2016), "…and the Cross-Section of Expected Returns"](https://people.duke.edu/~charvey/Research/Published_Papers/P118_and_the_cross.PDF) — applies multiple-testing haircuts to published factors; Review of Financial Studies 29(1), 5–68; author-hosted PDF.
- [Harvey & Liu (2018), "Detecting Repeatable Performance"](https://people.duke.edu/~charvey/Research/Published_Papers/P132_Detecting_repeatable_performance.pdf) — separates skill from luck in observed track records; Review of Financial Studies 31(7), 2499–2552; author-hosted PDF.
- [Bailey, Borwein, López de Prado & Zhu (2017), "The Probability of Backtest Overfitting"](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf) — introduces PBO, a framework for quantifying how likely a strategy-selection procedure is to pick noise; Journal of Computational Finance 20(4); author-hosted PDF.
- [Arnott, Harvey & Markowitz (2019), "A Backtesting Protocol in the Era of Machine Learning"](https://people.duke.edu/~charvey/Research/Published_Papers/P138_A_backtesting_protocol.pdf) — a checklist for in-sample/out-of-sample discipline before deploying a data-mined strategy; Journal of Financial Data Science 1(1), 2019; author-hosted PDF.
- [Bergmeir & Benítez (2012), "On the use of cross-validation for time series predictor evaluation"](https://doi.org/10.1016/j.ins.2011.12.028) — when plain k-fold cross-validation is legitimate for purely autoregressive time-series predictors, and when it leaks; Information Sciences 191, 192–213. (Note: publisher paywall.)

## Backtesting & validation libraries

- [vectorbt](https://github.com/polakowo/vectorbt) — vectorised backtesting and parameter-sweep engine built on NumPy/pandas/Numba. (Note: free community edition; the authors' development focus is the separate commercial vectorbt.PRO.)
- [mlfinlab](https://github.com/hudson-and-thames/mlfinlab) — Hudson & Thames' implementations of AFML techniques such as purged cross-validation and meta-labeling. (Note: no longer developed in the open — the repo is kept for issues and the library moved to a commercial licence; last commit October 2023.)
- [Qlib](https://github.com/microsoft/qlib) — Microsoft's AI-oriented quant research platform: data pipeline, factor and ML model workflows, and evaluation tooling.
- [cvxportfolio](https://github.com/cvxgrp/cvxportfolio) — portfolio construction and backtesting based on the multi-period trading framework of Boyd's Stanford group, built on convex optimization.

## Risk & portfolio optimization

- [PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt) — practical portfolio optimization: efficient frontier, Black–Litterman, hierarchical risk parity, covariance shrinkage.
- [skfolio](https://github.com/skfolio/skfolio) — portfolio optimization with scikit-learn conventions (estimators, pipelines, cross-validation) and a broad set of risk measures.
- [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) — optimization-based portfolio construction and risk budgeting over many risk measures, built on cvxpy.
- [QuantLib](https://github.com/lballabio/QuantLib) — the comprehensive open-source quant library for instrument pricing, yield curves and fixed-income analytics (C++ with Python bindings).

## Time-series ML & statistics

- [scikit-learn](https://github.com/scikit-learn/scikit-learn) — general-purpose machine learning in Python; its cross-validation, pipeline and calibration APIs are the reference toolkit for leakage-aware modeling.
- [statsmodels](https://github.com/statsmodels/statsmodels) — classical econometrics in Python: regression, ARIMA, hypothesis tests and time-series diagnostics.
- [arch](https://github.com/bashtage/arch) — ARCH/GARCH volatility models, unit-root tests and bootstrapping for Python, by Kevin Sheppard.
- [sktime](https://github.com/sktime/sktime) — unified framework for machine learning with time series, including forecasting and train/test splitters that respect temporal order.
- [darts](https://github.com/unit8co/darts) — forecasting library wrapping classical and deep models (ARIMA to N-BEATS/Transformers) behind one API, with backtesting utilities.

## Market data & datasets

- [yfinance](https://github.com/ranaroussi/yfinance) — unofficial downloader for Yahoo Finance market data; convenient for prototyping, not a stable production data source.
- [FRED](https://fred.stlouisfed.org) — St. Louis Fed database of macroeconomic and financial time series; free API access with registration. (Note: the site drops automated requests from datacenter IPs, so the CI link check skips it.)
- [Nasdaq Data Link](https://data.nasdaq.com) — data platform (formerly Quandl): some series free, most content commercial.
- [SEC EDGAR full-text search](https://www.sec.gov/edgar/search/) — free search over US regulatory filings and disclosures. (Note: sec.gov rate-limits automated requests; a user-agent header is required.)
- [ECB Data Portal](https://data.ecb.europa.eu/) — European Central Bank statistics (exchange rates, yields, prices); successor to the Statistical Data Warehouse.
- [WRDS](https://wrds-www.wharton.upenn.edu) — Wharton Research Data Services; CRSP/Compustat-class data behind an institutional academic subscription.
- [Jane Street Market Prediction (Kaggle)](https://www.kaggle.com/c/jane-street-market-prediction) — 2021 competition on anonymized features derived from real market data; a strong tabular-ML benchmark, not tradable signal.
- [OpenBB](https://github.com/openbq-org/OpenBB) — open-source data platform and workspace for investment research, aggregating many public data sources.

## Financial NLP

- [FinBERT](https://github.com/ProsusAI/FinBERT) — BERT model fine-tuned for financial sentiment classification (Prosus AI); a common open baseline for sentiment on finance text.
- [Loughran–McDonald word lists](https://sraf.nd.edu) — official home of the Loughran–McDonald financial sentiment dictionaries at Notre Dame's SRAF; free for research use.

## Community & learning

- [Quantitative Finance Stack Exchange](https://quant.stackexchange.com) — practitioner Q&A on derivatives, risk, backtesting and data. (Note: the site blocks automated requests; verified manually.)
- [arXiv q-fin](https://arxiv.org/list/q-fin/recent) — daily feed of new quantitative finance preprints across all subcategories.
- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — the long-running community list of quant and trading resources; broader than this list's research focus.
- [IDEAS / RePEc](https://ideas.repec.org) — aggregated working papers and published research in economics and finance.

## Companion research repos

Part of an open research portfolio by Aydin Monavvari — each repository states its own data sources, scope and limitations in its README; the one-liners below are summarized from those READMEs.

- [financial-ml-validation](https://github.com/aydinmonavvari/financial-ml-validation) — purged K-fold, walk-forward, PSR/DSR and calibration-aware thresholds as a small pip-installable library.
- [finance-data-analysis-lab](https://github.com/aydinmonavvari/finance-data-analysis-lab) — descriptive analytics and reproducible exploration of real daily market data, as an educational research project.
- [macro-forecasting-lab](https://github.com/aydinmonavvari/macro-forecasting-lab) — classical time-series models versus machine learning for US macro indicators under strict chronological validation, against naive baselines.
- [ml-market-prediction-study](https://github.com/aydinmonavvari/ml-market-prediction-study) — leakage-free, walk-forward study of whether daily equity data predicts next-day index direction; the headline finding is negative — and that is the point.
- [portfolio-optimization-lab](https://github.com/aydinmonavvari/portfolio-optimization-lab) — mean-variance and risk-parity construction with covariance shrinkage and transaction costs under walk-forward evaluation.
- [credit-risk-modeling](https://github.com/aydinmonavvari/credit-risk-modeling) — probability-of-default modeling on a public UCI dataset with calibration, cost-based thresholds and fairness diagnostics.
- [fraud-anomaly-detection](https://github.com/aydinmonavvari/fraud-anomaly-detection) — supervised versus unsupervised fraud detection under extreme class imbalance, with PR-AUC-first evaluation and a synthetic-data mode.
- [dl-financial-time-series](https://github.com/aydinmonavvari/dl-financial-time-series) — tiny deep sequence models versus classical baselines for next-day index direction, under walk-forward evaluation with leakage controls.
- [financial-nlp-sentiment](https://github.com/aydinmonavvari/financial-nlp-sentiment) — sentiment-classification benchmark on the Financial PhraseBank corpus comparing lexicon, TF-IDF, frozen embeddings and FinBERT.
- [fin-rag-research-assistant](https://github.com/aydinmonavvari/fin-rag-research-assistant) — retrieval-augmented question answering over Federal Reserve Beige Book reports, comparing BM25, dense and hybrid retrieval with citation-grounded generation.
- [finscope-ai-research](https://github.com/aydinmonavvari/finscope-ai-research) — integrating capstone of the portfolio: one full financial-research cycle on real public data, with documented limitations at every stage.

## Contributing

Improvements are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria, the annotation format, and how to run the offline structure test (`python tests/test_readme_structure.py`) before opening a pull request.

## License

Released under the MIT License — see [LICENSE](LICENSE).

---

Annotations reflect the author's reading as of 2026-11; the link check runs monthly in CI. Report dead links or propose additions via a pull request.

Listed in the spirit of [awesome](https://github.com/sindresorhus/awesome) — an independent list, not an official sindresorhus/awesome collection.
