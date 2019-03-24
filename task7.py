# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:24:53 2019

@author: X260
"""
import pandas as pd

all_tb = pd.read_csv('~/Downloads/TB_burden_countries_2019-01-11.csv', index_col = 0)

countries = all_tb['country']

#selecting Kenya data
kenya_data = all_tb.loc['Kenya']

all_tb.loc['Kenya' , 'e_inc_num'].describe().round()

#greater than column
all_tb[all_tb['e_inc_num'] > 30000]

