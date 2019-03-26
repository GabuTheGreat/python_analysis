# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:09:41 2019

@author: X260
"""

import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Importing TB data
all_tb = pd.read_csv ('~/Downloads/TB_burden_countries_2019-01-11.csv', encoding = 'utf-8')

#Descriptive statistics of TB data

all_tb.describe()

len(list(all_tb)) #ncolumns

len(all_tb.values) #nrows

all_tb ['country'].describe()

all_tb ['year'].describe()

#basic statistics for estimated number of incident cases (all forms)
all_tb ['e_inc_num'].describe().round()

all_tb ['e_inc_num'].sum()

#selecting necessary columns for data manipulation
all_tb_inc = all_tb[['country', 'year', 'e_inc_num', 'e_pop_num']] 

#sorting to get which countries have the highest/ lowest incidence in TB
all_tb_inc_sorted = all_tb_inc.sort_values(by = ['e_inc_num' , 'country'] , ascending = False)

#measure the rate of TB in country population
# Divide number of incident cases with the poplulation and create new column 
all_tb_inc_sorted['perc_rate_country_population'] = (all_tb_inc_sorted['e_inc_num']/all_tb_inc_sorted ['e_pop_num'] * 100) . round(2)

#Grouping data set by country and year 
summary= all_tb_inc_sorted.groupby (['country']).perc_rate_country_population.mean() . reset_index()

summary_2 = all_tb_inc_sorted.groupby (['country']).perc_rate_country_population.agg({("avarage_rate", "mean"),("Count", "count")})

#Calculating mean, median, min, max and quartiles

summary['perc_rate_country_population'].agg(['sum','max','min','median'])

summary['perc_rate_country_population'].describe (percentiles = [0.5, 0.75,0.25,0.8]).round(2)


#improved the plot
fig = plt.figure(figsize=(6,6)) # define plot area
ax = fig.gca() # define axis
summary['perc_rate_country_population'].plot.hist()
ax.set_title('Histogram of Rate') # Give the plot a main title
ax.set_xlabel("Rate") # Set text for the x axis
ax.set_ylabel("Frequency of Rate") # Set text for the x axis
plt.show()

