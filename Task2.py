# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:57:43 2019

@author: X260
"""

import pandas as pd

#Import TB data
all_tb = pd.read_csv ('~/Downloads/TB_burden_countries_2019-01-11.csv', encoding = 'utf-8')

#Descriptive statistics of TB data

all_tb.describe()

len(list(all_tb)) 

len(all_tb.values)

#Estimate incidence of TB cases who are HIV-positive
# Basic statistics 

all_tb ['e_inc_tbhiv_num'] .describe()

all_tb ['e_inc_tbhiv_num'] .sum()

tb_hiv_pos = all_tb [['country', 'year' , 'e_inc_tbhiv_num', 'e_pop_num']]

#calculating the rate of TB cases with HIV in country population
tb_hiv_pos['tb_hiv_pos_rate'] = (tb_hiv_pos['e_inc_tbhiv_num']/ tb_hiv_pos ['e_pop_num'] * 100) .round(2)

summary_tb = tb_hiv_pos.groupby(['country', 'year']) .tb_hiv_pos_rate.sum().reset_index()

summary_tb['tb_hiv_pos_rate'].agg(['sum','max','min','median'])

summary_tb['tb_hiv_pos_rate'].describe (percentiles = [0.5, 0.75,0.25]).round(2)

summary_tb['tb_hiv_pos_rate'].plot(kind = 'hist')


