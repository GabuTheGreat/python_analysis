# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:05:13 2019

@author: X260
"""

import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Importing TB data
all_tb = pd.read_csv ('~/Downloads/TB_burden_countries_2019-01-11.csv', encoding = 'utf-8')

all_tb = all_tb[['country','iso3']]

all_tb = all_tb.drop_duplicates(subset = ['country'])

len(all_tb ['country'].unique())

all_gdp_data = pd.read_csv ('~/Downloads/Metadata_Country_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_10515199.csv', encoding = 'utf-8')

all_gdp_data = all_gdp_data[['Country Code','IncomeGroup']]

#renaming country code 
all_gdp_data.rename(columns = {"Country Code": "iso3"}, inplace = True )
#merging TB data with GDP data
merged_data = pd.merge(all_tb,all_gdp_data, on = ['iso3'])

#countries not included on income data
not_included = pd.merge(all_tb, merged_data, on = ['iso3'], how = "left", indicator = True)
not_included = not_included.loc[not_included["_merge"] == "left_only"]
