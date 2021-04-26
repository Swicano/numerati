import csv

import pandas as pd
import numpy as np
import numerapi
import os




class DataWriter:
    def __init__(self):
       pass
   
    def upload_prediction(self, file_path = None, model_id = None, API_id = 1, tournament = 8):
        
        # Get details and more from a secret_.py file
        try:
            from Config.secret_ import secrets
        except ImportError:
            print("account details missing, please add them!")
            raise
            
        napi = numerapi.NumerAPI(secrets[f'API{API_id}_public_id'], secrets[f'API{API_id}_secret_key'])
        
        if file_path is None:
            file_path = os.path.join('Data')
            file_path = os.path.join(file_path, f'Numerai_{napi.get_current_round()}', 'prediction','example_predictions.csv')
            #TODO figure out exact prediction file location
        
        if model_id is None:
            model_id = napi.get_models()[secrets[f'API{API_id}_username']]
            
        napi.upload_predictions(file_path = file_path,tournament = tournament, model_id = model_id)   