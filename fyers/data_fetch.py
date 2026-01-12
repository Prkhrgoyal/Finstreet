import pandas as pd

def fetch_ohlcv(fyers, symbol, start, end):
    data = {
        "symbol": symbol,
        "resolution": "D",
        "date_format": "1",
        "range_from": start,
        "range_to": end,
        "cont_flag": "1"
    }

    response = fyers.history(data)
    candles = response["candles"]

    df = pd.DataFrame(
        candles,
        columns=["timestamp", "open", "high", "low", "close", "volume"]
    )

    df["date"] = pd.to_datetime(df["timestamp"], unit="s")
    df.set_index("date", inplace=True)
    df.drop(columns="timestamp", inplace=True)

    return df
