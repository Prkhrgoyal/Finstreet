from strategy.features import compute_features
from strategy.model import train_model
from strategy.signal import forecast_volatility, build_signal

def generate_5day_signals(df, threshold):
    X, y = compute_features(df)
    model = train_model(X, y)

    prob = model.predict_proba(X.iloc[-1:])[0, 1]
    sigma = forecast_volatility(df["close"].pct_change().dropna())

    signals = []
    for i in range(1, 6):
        signals.append({
            "Day": f"T+{i}",
            "Probability_Up": prob,
            "Volatility": sigma,
            "Signal": build_signal(prob, sigma, threshold)
        })
    return signals
