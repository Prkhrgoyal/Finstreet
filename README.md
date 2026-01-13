# FYERS ML Trading System (Paper Trading)

Finstreet – FYERS ML Trading System

Finstreet Case Competition | Round 2 | FYERS Integration

This repository contains an end-to-end machine learning–driven trading system built as part of the Finstreet Case Competition, integrating FYERS API for market data access and trade execution.

The project strictly follows the competition requirements:

FYERS API–only data and execution

Daily OHLCV data

Chronological walk-forward backtesting

No manual intervention after initial setup

1. System Overview

The pipeline implemented in this repository is:

FYERS API (Historical Data)
        ↓
Feature Engineering
        ↓
ML Model Training
        ↓
5-Day Ahead Return / Direction Prediction
        ↓
Trading Signal Generation
        ↓
Risk Management Rules
        ↓
Backtesting / Execution (FYERS API)
        ↓
Portfolio Performance Evaluation

2. Project Structure
Finstreet/
│
├── fyers/                 # FYERS API authentication & client
│   └── auth.py
│
├── strategy/              # ML model and signal logic
├── backtest/              # Walk-forward backtesting
│
├── main.py                # Single entry point for execution
├── config.py              # FYERS credentials (user-provided)
├── requirements.txt       # Dependencies
├── README.md
└── .gitignore

3. Environment Setup
Step 1: Clone the Repository
git clone https://github.com/Prkhrgoyal/Finstreet.git
cd Finstreet

Step 2: Create and Activate Virtual Environment
python -m venv venv


Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

4. FYERS API Setup (Mandatory)

This project requires FYERS API credentials to run.

Step 4.1: Create FYERS App

Visit: https://myapi.fyers.in/

Create a new app with:

App Type: Web App

Redirect URI:

http://127.0.0.1:5000/callback


You will receive:

Client ID (App ID)

Secret Key

Step 4.2: Create config.py

Create a file named config.py in the project root:

FYERS_CLIENT_ID = "YOUR_APP_ID"        # e.g. ABCD12-100
FYERS_SECRET_KEY = "YOUR_SECRET_KEY"
FYERS_REDIRECT_URI = "http://127.0.0.1:5000/callback"


⚠️ config.py is intentionally not tracked in GitHub for security reasons.

5. Execution Instructions (Complete Pipeline)
Step 5.1: Run the System
python main.py

Step 5.2: FYERS Authentication Flow

A browser window opens automatically.

Log in using FYERS credentials.

After login, you will be redirected to:

http://127.0.0.1:5000/callback?auth_code=XXXXXX


Copy the auth_code from the URL.

Paste it into the terminal when prompted.

✔ Authentication is now complete.

Step 5.3: Automated Pipeline Execution

After authentication:

Historical data is fetched using FYERS API

Feature engineering is applied

ML model is trained

5-day ahead predictions are generated

Trading signals are created

Risk management rules are applied

Walk-forward backtest is executed

Portfolio metrics are computed

No further manual input is required.

6. Compliance With Competition Constraints

✔ FYERS API used for data & execution
✔ Only daily OHLCV data
✔ No external or proprietary datasets
✔ Chronological backtesting (no data leakage)
✔ Fully reproducible execution

7. Notes for Evaluators

Authentication is required once per session due to FYERS security policies.

All trading logic and data access strictly use FYERS APIs.

The codebase is modular and documented for clarity and reproducibility.
