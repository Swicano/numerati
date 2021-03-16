from xgboost import XGBRegressor

class ModelSelector:
    def __init__(self, modelName):
        self.modelName = modelName

    def select(self):
        if self.modelName == 'xgboost':
            return self.xgboost()

    def xgboost(self):
        return XGBRegressor(max_depth=5, learning_rate=0.1, n_estimators=20, n_jobs=-1, colsample_bytree=0.1)
