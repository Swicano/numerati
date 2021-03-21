import csv


import pandas as pd
import numpy as np


class DataReader:
    def __init__(self):
       pass

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