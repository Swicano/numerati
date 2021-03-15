import csv

import pandas as pd
import numpy as np
from xgboost import XGBRegressor

TARGET_NAME = f"target"
PREDICTION_NAME = f"prediction"

MODEL_FILE = Path("example_model_1.xgb")

class XGBoost1:
    def __init__(self):
        self.model_name = 'XGBRegressor'

    def getTrainingData(self,  filename):
        print("loading training data...")
        training_data = self.read_csv(filename)

    def getTournamentData(self, filename):
        print("loading tournament data...")
        training_data = self.read_csv(filename)
