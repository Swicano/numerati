#!/usr/bin/env python
import argparse
from Model.example_model_1  import example_class

class Main:
    """
    idk what I'm doing I'm just stressed out + sunday scaries so I am writing this
    first cli for numereati
    """
    def __init__(self):
        self.some_attribute = 'this is an attribute, be default, on the class Main'


    def sayHi(self):
        print('hi')





class Predict:
    pass

class Visualize:
    pass


if __name__ == "__main__":


    parser = argparse.ArgumentParser(description="the numereati converge")

    parser.add_argument(
        "-",
        "--file",
        help = "inject a file",
        default = None
    )
    parser.add_argument(
        "-m",
        "--model",
        help = "select the model to train",
        default = None
    )
    parser.add_argument(
        "-t",
        "--training_data",
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

    newMain = Main()
    newMain.sayHi()
    print('data:', args.data)
    print('model:', args.model)
    print()
