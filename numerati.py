#!/usr/bin/env python
import argparse
import csv
from pathlib import Path

import numpy as np
import pandas as pd

from Model.model_selector import ModelSelector


MODEL_FILE = Path("Model/trained_models/xgboost1.xgb")
TARGET_NAME = f"target"
PREDICTION_NAME = f"prediction"


class Model:
    """
    top level run the modeling
    """
    def __init__(self, modelName, trainingDataFileName):
        self.modelName = modelName
        self.trainingDataFileName = trainingDataFileName

    def getData(self):
        return self.read_csv("Data/example_model_1/numerai_training_data.csv")

    def read_csv(self, file_path):
        with open(file_path, 'r') as f:
            column_names = next(csv.reader(f))

        dtypes = {x: np.float16 for x in column_names if x.startswith(('feature', 'target'))}
        df = pd.read_csv(file_path, dtype=dtypes, index_col=0)

        # Memory constrained? Try this instead (slower, but more memory efficient)
        # see https://forum.numer.ai/t/saving-memory-with-uint8-features/254
        # dtypes = {f"target": np.float16}
        # to_uint8 = lambda x: np.uint8(float(x) * 4)
        # converters = {x: to_uint8 for x in column_names if x.startswith('feature')}
        # df = pd.read_csv(file_path, dtype=dtypes, converters=converters)

        return df

    def train(self):

        model = ModelSelector(self.modelName)
        selectedModel = model.select()

        trainingData  = self.getData()
        feature_names = [
            f for f in trainingData.columns if f.startswith("feature")
        ]

        if MODEL_FILE.is_file():
            print("Loading pre-trained model...")
            selectedModel.load_model(MODEL_FILE)
        else:
            print("Training model...")
            selectedModel.fit(trainingData[feature_names], trainingData[TARGET_NAME])
            selectedModel.save_model(MODEL_FILE)


class Predict:
    pass

class Visualize:
    pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="the numereati converge")
    parser.add_argument(
        "-m",
        "--modelName",
        help = "select the model to train",
        default = 'xgboost'
    )
    parser.add_argument(
        "-t",
        "--trainingDataFileName",
        help = "select the data set on which to train the model",
        default = None
    )
    parser.add_argument(
        "-p",
        "--predict_data",
        help = "select the data set on which to usee the",
        default = None
    )

    args = parser.parse_args()

    modelName = args.modelName
    trainingDataFileName = args.trainingDataFileName

    newModel = Model(modelName, trainingDataFileName)
    newModel.train()