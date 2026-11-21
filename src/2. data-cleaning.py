"""
Created on Thu Feb  8 22:12:00 2024

@author: firas-alameddine-795
"""

import pandas as pd
import numpy as np
df = pd.read_csv("df.csv", dtype = 'object')

# %% Clean numbers from special characters
df['year'] = df['year'].astype("int64")
df['hs6_code'] = df['hs6_code'].str.replace('\.', '', regex=True)\
                               .astype("int64")
df['trade_value_lbp'] = df['trade_value_lbp'].str.replace('\,', '', regex=True)\
                                             .astype("int64")
df['trade_value_usd'] = df['trade_value_usd'].str.replace('\,', '', regex=True)\
                                             .astype("int64")
df['trade_value_kg'] = df['trade_value_kg'].str.replace('\,', '', regex=True)\
                                           .astype("int64")

# %% Convert HS6 from "As Reported" to "HS92"
convert_07_92 = pd.read_excel('data - lebanese customs/HS 2007 to HS 1992 Correlation and conversion tables.xls')
convert_12_92 = pd.read_excel('data - lebanese customs/HS 2012 to HS 1992 Correlation and conversion tables.xls')
convert_17_92 = pd.read_excel('data - lebanese customs/HS 2017 to HS 1992 Correlation and conversion tables.xlsx')

# Make column names consistent
convert_12_92.columns = ['From','To']
convert_17_92.columns = ['From','To']

#Create a mapping dictionary out of each file. (i.e. convert dataframes to dictionaries)

conv1 = {}
for pair in convert_07_92.to_dict('records'):
    conv1[pair['From']] = pair['To']
    
conv2 = {}
for pair in convert_12_92.to_dict('records'):
    conv2[pair['From']] = pair['To']

conv3 = {}
for pair in convert_17_92.to_dict('records'):
    conv3[pair['From']] = pair['To']

df_copy = df

def convert_code(dataset):
    """
    This fuction uses two columns of the Lebanese Customs dataframe as inputs: Year, and HS6 Code. 
    Then it checks the year and in which period it should be. We already know there are three possible periods to look 
    for: between 2007 and 2012, between 2012 and 2017, and after 2017. After knowing this information, the fuction 
    converts the code using one of the dictionaries created earlier, depending on the corresponding period. The output
    is the new code.
    Please noted that some codes may not exist in the csv files we just read (i am speaking of codes in chapter 98 which
    is used for national purposes and thus does not have an international definition).
    """
    # Create masks for each year range
    mask_2011 = dataset['year'] == 2011
    mask_2012_2016 = dataset['year'].between(2012, 2016)
    mask_2017_2019 = dataset['year'].between(2017, 2019)

    # Use vectorized operations to update values based on masks
    dataset['new_hs6_code'] = dataset['hs6_code']  # Set initial values as the original codes
    dataset.loc[mask_2011, 'new_hs6_code'] = dataset.loc[mask_2011, 'hs6_code']\
                                                    .map(conv1.get)
    dataset.loc[mask_2012_2016, 'new_hs6_code'] = dataset.loc[mask_2012_2016, 'hs6_code']\
                                                         .map(conv2.get)
    dataset.loc[mask_2017_2019, 'new_hs6_code'] = dataset.loc[mask_2017_2019, 'hs6_code']\
                                                         .map(conv3.get)

    # Fill missing values with original codes (might be optimizable, see note below)
    dataset['new_hs6_code'].fillna(dataset['hs6_code'], inplace=True)
    dataset['new_hs6_code'] = dataset['new_hs6_code'].astype(pd.Int64Dtype())

    return dataset

# Apply the covert_code() function.
df = convert_code(df)

# Delete the old HS6 Codes column, and rename the new one.
df = df.drop('hs6_code', axis = 1)\
       .rename(columns = {'new_hs6_code':'hs6_code'})\
       .sort_values(by = ['trade_flow', 'year', 'country', 'hs6_code'])

# %% Arrange columns in a suitable manner
df = df[['year','country','trade_flow','hs6_code','trade_value_usd','trade_value_lbp','trade_value_kg']]

# %% Extract HS2 and HS4 Codes out of HS6 Codes.
df.insert(loc = 3, 
          column = 'hs4_code',
          value = df['hs6_code'].apply(lambda x: np.floor(x/100).astype(np.int64)))

df.insert(loc = 3, 
          column = 'hs2_code', 
          value = df['hs6_code'].apply(lambda x: np.floor(x/10000).astype(np.int64)))

# %% Map HS1 Codes out of HS2 Codes.

section_list = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI',
                'XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX',
                'XXI']

chapters_list = [[1,2,3,4,5],[6,7,8,9,10,11,12,13,14],[15],
       [16,17,18,19,20,21,22,23,24],[25,26,27],
       [28,29,30,31,32,33,34,35,36,37,38],[39,40],
       [41,42,43],[44,45,46],[47,48,49],
       [50,51,52,53,54,55,56,57,58,59,60,61,62,63], 
       [64,65,66,67],[68,69,70],[71],
       [72,73,74,75,76,77,78,79,80,81,82,83],[84,85],
       [86,87,88,89],[90,91,92],[93],[94,95,96],
       [97,98]]


hs2_hs1 = {}
for section, codelist in zip(section_list, chapters_list):
    for code in codelist:
        hs2_hs1[code] = section
        
hs2_hs1 = {code: section_list[i] for i, codelist in enumerate(chapters_list) for code in codelist}
df.insert(loc = 3, 
          column = 'hs1_code', 
          value = df['hs2_code'].map(hs2_hs1))

# %% Save to csv
df.to_csv("df.csv")
