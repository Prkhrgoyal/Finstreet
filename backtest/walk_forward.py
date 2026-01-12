from strategy.features import compute_features
from strategy.model import train_model
from strategy.signal import forecast_volatility, build_signal
import config

def walk_forward(df):
    pnl = []
    for t in range(30, len(df) - 1):
        train = df.iloc[:t]
        X, y = compute_features(train)
        model = train_model(X, y)

        prob = model.predict_proba(X.iloc[-1:])[0, 1]
        sigma = forecast_volatility(train["close"].pct_change().dropna())
        signal = build_signal(prob, sigma, config.SIGNAL_THRESHOLD)

        ret = (df["close"].iloc[t + 1] - df["close"].iloc[t]) / df["close"].iloc[t]
        pnl.append(signal * ret)
    return pnl
