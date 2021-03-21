#!/usr/bin/env python
import argparse
import csv
from pathlib import Path

from Model.model_selector import ModelSelector
from DataHandlers.data_reader import DataReader

MODEL_FILE = Path("Model/trained_models/xgboost1.xgb")
TARGET_NAME = f"target"
PREDICTION_NAME = f"prediction"


class Main:
    """

    top level run the modeling

    """
    def __init__(self, modelName, trainingDataFileName):
        self.modelName = modelName
        self.trainingDataFileName = trainingDataFileName

    def readData(self):
        dataReader = DataReader()
        return dataReader.read_csv("Data/example_model_1/numerai_training_data.csv")

    def train(self):

        model = ModelSelector(self.modelName)
        selectedModel = model.select()


        trainingData  = self.readData()
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

    newRun = Main(modelName, trainingDataFileName)

    newRun.train()
