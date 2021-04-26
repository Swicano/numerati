# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:59:01 2021

@author: gabo
"""

import numerapi
import os

# Get details and more from a secret_.py file
try:
    from Model.secret_ import secrets
except ImportError:
    print("account details missing, please add them there!")
    raise
    
napi = numerapi.NumerAPI(secrets['API1_public_id'], secrets['API1_secret_key'])

# download data
napi.download_current_dataset( dest_path=os.path.join('..','Data','bob'), dest_filename='test.zip', unzip=True)


# download data
napi.signalsapi.download_validation_data( dest_path=os.path.join('..','Data'), dest_filename='valid.zip', unzip=True)

sapi = numerapi.SignalsAPI();
sapi.download_validation_data(dest_path=os.path.join('..','Data'), dest_filename='valid.zip')


