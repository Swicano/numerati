from Model.scripts.xgboost1 import XGBoost

class ModelSelector:
    def __init__(self, modelName):
        self.modelName = modelName

    def select(self):
        if self.modelName == 'xgboost':
            XGBoost1  = XGBoost()
            return XGBoost1.xgboost1()
