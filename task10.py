# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:04:08 2019

@author: X260
"""

import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Importing TB data
all_tb = pd.read_csv ('~/Downloads/TB_burden_countries_2019-01-11.csv', encoding = 'utf-8')

# Selecting required columns

all_tb = all_tb[['country' , 'year' , 'g_whoregion', 'e_inc_num' , 'e_pop_num']]

all_tb['g_whoregion'].unique()

#Incurrence per pop

all_tb['perc_rate'] = (all_tb['e_inc_num']/all_tb['e_pop_num'] * 100 ).round(2)

#select countries in Africa region

all_afr = all_tb.loc[all_tb['g_whoregion']=='AFR',['year', 'country', 'perc_rate']]

#select countries in West Pacific region

all_wpr = all_tb.loc[all_tb['g_whoregion']=='WPR',['year', 'country', 'perc_rate']]

#select countries in South East Asia region

all_sea = all_tb.loc[all_tb['g_whoregion']=='SEA',['year', 'country', 'perc_rate']]

#select countries in Europe region

all_eur = all_tb.loc[all_tb['g_whoregion']=='EUR',['year', 'country', 'perc_rate']]

#select countries in Eastern Mediterranean Region region

all_emr = all_tb.loc[all_tb['g_whoregion']=='EMR',['year', 'country', 'perc_rate']]

#select countries in America region

all_amr = all_tb.loc[all_tb['g_whoregion']=='AMR',['year', 'country', 'perc_rate']]

#group by country

all_afr.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', figsize=(10,2))
all_sea.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', figsize=(10,2))
all_wpr.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', figsize=(10,2))
all_eur.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', figsize=(10,2))
all_emr.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', figsize=(10,2))
all_amr.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', figsize=(10,2))

#Combined subplots
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20,15))

# Divide the figure into a 2x1 grid, and give me the first section
ax1 = axes[0][0]
ax2 = axes[0][1]
ax3 = axes[0][2]
ax4 = axes[1][0]
ax5 = axes[1][1]
ax6 = axes[1][2]


all_afr.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', ax=ax1, figsize=(5,10))
all_sea.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', ax=ax2, figsize=(5,10))
all_wpr.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', ax=ax3, figsize=(10,2))
all_eur.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', ax=ax4, figsize=(10,2))
all_emr.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', ax=ax5, figsize=(10,2))
all_amr.groupby('country')['perc_rate'].mean().sort_values().plot(kind='barh', ax=ax6, figsize=(10,2))