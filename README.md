# Finstreet
FYERS ML Trading System (Paper Trading)

Overview

This repository implements an end-to-end machine learning–driven trading system for FYERS Presents AQUA – KSHITIJ 2026 (Round 2).

Pipeline: FYERS Data → Feature Engineering → ML Model → Signals → Paper Trades → Walk-Forward Backtest → Performance Metrics

The strategy prioritizes signal quality, risk management, and reproducibility over raw profit.


---

Stock & Data

Stock: IRCON International Ltd (IRCON.NS)

Data Source: FYERS Official API

Period: 1 Nov 2025 – 31 Dec 2025

Frequency: Daily

Columns: Open, High, Low, Close, Volume only


No external or alternative datasets are used.


---

Strategy Summary

Model: Logistic Regression (L1-regularized) for directional prediction

Target: Next-day price direction (Up / Down)

Risk Model: GARCH(1,1) for volatility forecasting

Signal:


\text{Signal} = \frac{P(\text{Up}) - 0.5}{\sigma}

Trading actions:

BUY if signal > threshold

SELL if signal < −threshold

Otherwise, no trade



---

Risk Management

Volatility-based position sizing

Maximum risk capped at 1% of capital per trade

Automatic exposure reduction during high-volatility periods



---

Backtesting

Method: Chronological walk-forward backtest

No data leakage or look-ahead bias

Metrics: Net PnL, Sharpe Ratio, Maximum Drawdown, Directional Accuracy


The strategy is evaluated primarily on risk-adjusted performance (Sharpe).


---

Repository Structure

fyers-ml-trading-system/
├── fyers/        # FYERS auth, data fetch, paper orders
├── strategy/     # Features, model, signal logic
├── backtest/     # Walk-forward backtest & metrics
├── outputs/      # Signals, trades, PnL
├── docs/         # Explanation PDF
├── main.py
└── README.md


---

How to Run

pip install -r requirements.txt
python main.py


---

Compliance

Uses FYERS API for data and execution logic

Fully systematic, no manual intervention

Reproducible and modular codebase



