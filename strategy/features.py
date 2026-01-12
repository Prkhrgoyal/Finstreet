import numpy as np

def compute_features(df):
    df = df.copy()

    df["ret_1"] = np.log(df["close"]).diff()
    df["ret_3"] = df["ret_1"].rolling(3).mean()
    df["ret_5"] = df["ret_1"].rolling(5).mean()
    df["vol_5"] = df["ret_1"].rolling(5).std()
    df["vol_10"] = df["ret_1"].rolling(10).std()
    df["vol_chg"] = np.log(df["volume"]).diff()

    df["target"] = (df["ret_1"].shift(-1) > 0).astype(int)
    df.dropna(inplace=True)

    X = df[["ret_1", "ret_3", "ret_5", "vol_5", "vol_10", "vol_chg"]]
    y = df["target"]

    return X, y
