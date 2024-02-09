# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 21:17:33 2024

@author: firas-alameddine-795
"""

import pandas as pd
import glob

# %% Read files
filenames = glob.glob('data - lebanese customs/lebanese customs yearly HS6 *.xlsx')
dfs = [pd.read_excel(f, dtype='object') for f in filenames]
df = pd.concat(dfs, ignore_index=True)
del dfs

# Rename columns
df = df.rename(columns = {'hs_code':'hs6_code'})

# %% Melt dataset by trade flow
lebimport = df[['year','country','hs6_code','import_lbp','import_usd','import_kg']]
lebimport.insert(loc = 2, column = 'trade_flow', value = 'import')
lebimport = lebimport.rename(columns = {'import_lbp':'trade_value_lbp',
                                        'import_usd':'trade_value_usd',
                                        'import_kg':'trade_value_kg'})

lebexport = df[['year','country','hs6_code','export_lbp','export_usd','export_kg']]
lebexport.insert(loc = 2, column = 'trade_flow', value = 'export')
lebexport = lebexport.rename(columns = {'export_lbp':'trade_value_lbp',
                                        'export_usd':'trade_value_usd',
                                        'export_kg':'trade_value_kg'})

df = pd.concat([lebimport, lebexport])
del lebimport
del lebexport

# %% Save to csv
df.to_csv("df.csv")