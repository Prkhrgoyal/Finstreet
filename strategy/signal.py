from arch import arch_model
import numpy as np

def forecast_volatility(returns):
    model = arch_model(returns * 100, vol="Garch", p=1, q=1, mean="Zero")
    res = model.fit(disp="off")
    sigma = np.sqrt(res.forecast(horizon=1).variance.values[-1][0]) / 100
    return sigma

def build_signal(prob, sigma, threshold):
    raw = (prob - 0.5) / sigma
    if raw > threshold:
        return 1
    elif raw < -threshold:
        return -1
    return 0
