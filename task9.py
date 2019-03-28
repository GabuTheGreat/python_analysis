# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:27:38 2019

@author: X260
"""

import pandas as pd

import numpy as np

import datetime

import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Importing TB data
all_tb = pd.read_csv ('~/Downloads/TB_burden_countries_2019-01-11.csv', encoding = 'utf-8')

# Selecting required columns

all_tb = all_tb[['country' , 'year', 'e_inc_num' , 'e_pop_num']]

all_tb['e_pop_num'].dtype

#store population as numpy array

np_pop = np.array('e_inc_num')

all_tb.plot.scatter( x = 'year' , y =  'e_inc_num' , s = np_pop)

df = pd.DataFrame(all_tb)

plt.scatter(df.year, df.e_inc_num)

#plotting singles separately
all_tb.groupby('country').plot(kind = 'barh', x='year', y='e_inc_num')

#plotting the singles together
fig, ax = plt.subplots()
all_tb.groupby('country').plot( x='year', y='e_inc_num', ax=ax, legend=False)


df.groupby('country')['e_inc_num'].mean().sort_values().plot(kind='barh', figsize=(10,2))

#Combined subplots
fig = plt.figure()

# Divide the figure into a 2x1 grid, and give me the first section
ax1 = fig.add_subplot(211)

# Divide the figure into a 2x1 grid, and give me the second section
ax2 = fig.add_subplot(212)

all_tb.groupby('country').plot(x='year', y='e_inc_num', ax=ax1, legend=False)
all_tb.groupby('country')['e_inc_num'].mean().sort_values().plot(kind='barh', ax=ax2)

df = pd.DataFrame(np.random.randn(10,2), columns=['col1','col2'])
df['col3'] = np.arange(len(df))**2 * 100 + 100


# group by countries

all_tb_b =all_tb.groupby(['country'], as_index=False).agg({'e_inc_num': 'sum', 'e_pop_num': 'sum'})


all_tb_d = all_tb.groupby('country').e_pop_num.mean().reset_index()
