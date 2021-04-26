import csv

import pandas as pd
import numpy as np
import numerapi
import os


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
    
    def download_dataset(self, file_path = None, overwrite = False):
                
        # Get details and more from a secret_.py file
        try:
            from Config.secret_ import secrets
        except ImportError:
            print("account details missing, please add them!")
            raise
            
        napi = numerapi.NumerAPI(secrets['API1_public_id'], secrets['API1_secret_key'])
            
        if file_path is None:
            file_path = os.path.join('Data')
            file_path = os.path.join(file_path, f'Numerai_{napi.get_current_round()}')
        
        if overwrite or not (os.path.exists(os.path.join(file_path, 'dataset.zip') )):
            # download data
            napi.download_current_dataset( file_path, dest_filename='dataset.zip', unzip=True)
        
        #delete zip file afterwards
        #                       # jk, we might want to keep these around     
        os.remove(os.path.join(file_path, 'dataset.zip'))