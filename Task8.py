# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:03:44 2019

@author: X260
"""

import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Importing TB data
all_tb = pd.read_csv ('~/Downloads/TB_burden_countries_2019-01-11.csv', encoding = 'utf-8')

#selecting necessary columns

all_tb = all_tb[['country', 'year' , 'g_whoregion', 'e_inc_num', 'e_pop_num']]

#measure the rate of TB in country population
# Divide number of incident cases with the poplulation and create new column 
all_tb['perc_rate'] = (all_tb['e_inc_num']/all_tb['e_pop_num'] * 100) . round(2)

#Grouping by country
all_tb_group = all_tb.groupby(['country', 'g_whoregion'] ).perc_rate.mean().reset_index()

summary = all_tb_group.groupby('g_whoregion')['perc_rate'].sum()

import matplotlib.patches as mpatches

summary.plot(kind='bar', rot = 0)
AFR = mpatches.Patch(label='Africa')
AMR = mpatches.Patch(label='America')
EMR = mpatches.Patch(label='emr')
EUR = mpatches.Patch(label='Europe')
plt.legend(handles=[AFR,AMR,EMR,EUR], loc=1)
plt.show()

#Rename series
summary.rename(columns = {"g_whoregion":"Continent", "perc_rate":"Rate of Incurrence"}, inplace = True)

summary.plot(kind='bar')
plt.show()
