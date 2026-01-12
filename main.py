from fyers.auth import authenticate
from fyers.data_fetch import fetch_ohlcv
from strategy.generate_signals import generate_5day_signals
from backtest.walk_forward import walk_forward
from backtest.metrics import sharpe, max_drawdown
import config

if __name__ == "__main__":
    fyers = authenticate()

    df = fetch_ohlcv(
        fyers,
        "NSE:IRCON-EQ",
        "2025-11-01",
        "2025-12-31"
    )

    signals = generate_5day_signals(df, config.SIGNAL_THRESHOLD)
    print("5-Day Signals:", signals)

    pnl = walk_forward(df)
    print("Sharpe:", sharpe(pnl))
    print("Max Drawdown:", max_drawdown(pnl))
