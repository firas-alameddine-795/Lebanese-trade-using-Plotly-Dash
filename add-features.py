# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:55:00 2024

@author: firas-alameddine-795
"""

import pandas as pd

df = pd.read_csv('df.csv')
# Add description
hs92 = pd.read_excel('data - lebanese customs/products_hs_92.xlsx', sheet_name = 'products_hs_92')
sections = pd.read_excel('data - lebanese customs/products_hs_92.xlsx', sheet_name = 'sections')

# %% Create a mapping dictionary. 
# In other words, convert the pandas dataframes into dictionaries.
get_names_hs92 = {}
for pair in hs92.to_dict('records'):
    get_names_hs92[pair['hs92']] = pair['name']
    
get_names_sections = {}
for pair in sections.to_dict('records'):
    get_names_sections[pair['section']] = pair['name']
    
# %% HS6 Description, missing description for these codes are fetched manually
# [980100, 980300, 980400, 980200, 710820, 980500]
df.insert(loc = 7, 
          column = 'hs6_desc', 
          value = df['hs6_code'].map(get_names_hs92)) 

missing = {710820:'Monetary Gold',
           980100:'Used furniture and household appliances and person',
           980200:'Trousseaux of newly-weds and students',
           980300:'Samples of no commercial value',
           980400:'Occasional giftsand personal dispatches',
           980500:'Caskets and coffins containing the body of a deceased'}

df['hs6_desc'] = df['hs6_desc'].fillna(df['hs6_code'].map(missing))

# %% HS4 Description, missing description for these codes are fetched manually
# [9801, 9803, 9804, 9802, 9805]
df.insert(loc = 6, 
          column = 'hs4_desc', 
          value = df['hs4_code'].map(get_names_hs92))
missing = {9801:'Used furniture and household appliances and person',
           9802:'Trousseaux of newly-weds and students',
           9803:'Samples of no commercial value',
           9804:'Occasional giftsand personal dispatches',
           9805:'Caskets and coffins containing the body of a deceased'}

df['hs4_desc'] = df['hs4_desc'].fillna(df['hs4_code'].map(missing))

# %% HS2 Description, missing description for these codes are fetched manually
# [98]
df.insert(loc = 5, 
          column = 'hs2_desc', 
          value = df['hs2_code'].map(get_names_hs92))
df['hs2_desc'] = df['hs2_desc'].fillna('Used furniture and household appliances and person')

# HS1 Description, no missing description
df.insert(loc = 4, column = 'hs1_desc', value = df['hs1_code'].map(get_names_sections))

# %%Add Region
regions = pd.read_excel('data - lebanese customs/country to region.xlsx')

# Create a map, with countries as key, and corresponding regions as values.
dic = {}
for record in regions.to_dict('records'):
    dic[record['Country']] = record['Region']
    if record['Country'] == 'Bahrain':
        dic[record['Country']] = 'Middle east'
    if record['Region'] == 'Arab States' and record['Country'] != 'Bahrain':
        dic[record['Country']] = 'Africa'

# Insert a new column 'Region'
df.insert(loc = 2, column = 'region', value = df['country'].map(dic))

# Lots of countries do not have their region reported. 
values = {'Duty Free-Airport':'Misc', 
          'Falkland Islands':'South/Latin America', 
          'Free Zone':'Misc',
          'French South Territories':'Misc',
          'Guinea- Bissau':'Africa',
          'Heard  Mcdonald Islands':'Misc', 
          'Holy See (Vatican city st':'Europe',
          'Indian Ocean Territories':'Misc',
          'Iran, Islamic republic of':'Middle east',
          'Ivory Coast':'Africa',
          'Kazakstan':'Asia & Pacific',
          "Korea,Democ. People's rep":'Asia & Pacific',
          'Kosovo':'Europe',
          "Lao People's Dem Republic":'Asia & Pacific',
          'Lebanon-returned Goods':'Misc',
          'Libyan Arab Jamahiriya':'Africa', 
          'Misc':'Misc',
          'Neutral Zone':'Misc',
          'Northern Mariana islands':'Misc',
          'Saint kitts & nevis':'South/Latin America',
          'Serbia & Montenegro':'Europe',
          'Ship Supplies':'Misc',
          'Soolmon Islands':'Asia & Pacific',
          'Svalbard&Jan Mayen':'Europe',
          'Taiwan, Province of china':'Asia & Pacific',
          'Tanzania, United Republic':'Africa',
          'Trinidad & Tobago':'South/Latin America',
          'Turks&caicos Islands':'South/Latin America',
          'Viet Nam':'Asia & Pacific',
          'Virgin Island, U.S':'South/Latin America',
          'Warehouse':'Misc',
          'Yugoslavia':'Europe',
          'Zaire':'Africa',
          'Christmas island':'Misc',
          'Cocos Islands':'Misc',
          'Micronesia,Federation':'Misc',
          'Palestine terri, Occupied':'Middle east',
          'Saint Vincent&grenadines':'South/Latin America',
          'Wallis and  Futuna':'Asia & Pacific',
          'Pitcairn':'Asia & Pacific',
          'Saint Pierre & Miquelon':'North America',
          'East Timor':'Asia & Pacific',
          'Airline Supplies':'Misc',
          'Ceuta':'Europe',
          'Us Minor Outlying Islands':'Misc'}

df['region'] = df['region'].fillna(df['country'].map(values))

# %% Save file to csv
df.to_csv("df.csv")
