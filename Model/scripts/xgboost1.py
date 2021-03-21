from xgboost import XGBRegressor


class XGBoost:
    def __init__(self):
        pass

    def xgboost1(self):
        return XGBRegressor(max_depth=5, learning_rate=0.1, n_estimators=20, n_jobs=-1, colsample_bytree=0.1)
