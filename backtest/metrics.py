import numpy as np

def sharpe(pnl):
    pnl = np.array(pnl)
    return np.sqrt(252) * pnl.mean() / pnl.std()

def max_drawdown(pnl):
    cum = pnl.cumsum()
    peak = np.maximum.accumulate(cum)
    return (cum - peak).min()
