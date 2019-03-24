# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:40:20 2019

@author: X260
"""

import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('ggplot')

all_tb = pd.read_csv('~/Downloads/TB_burden_countries_2019-01-11.csv' , encoding = 'utf-8')
                     
#Descriptive statistics of TB data

all_tb .describe()

len(list(all_tb))

len(all_tb.values)

#Comparison of TB incurrence in the population of people with HIV compared to people without HIV.
# Basic statistics 

all_tb['e_inc_num'] .describe().round()

all_tb['e_inc_tbhiv_num'].describe()

#Select required columns

tb_pos_neg_rate = all_tb[['country', 'year', 'e_inc_num', 'e_inc_tbhiv_num']]

#Get column with people with TB and are HIV negative 
#Substract column of all cases of TB incidences and TB incidences with HIV
tb_pos_neg_rate['tb_hiv_neg'] = all_tb['e_inc_num'] - all_tb['e_inc_tbhiv_num'] 

#Box plot for two variable for Kenya
box_plot_data = tb_pos_neg_rate.loc[tb_pos_neg_rate['country'] == "Kenya", ['e_inc_tbhiv_num', 'e_inc_num']]
box_plot_data.plot.box()

#box plot for two countries, same variable
box_plot_kenya = tb_pos_neg_rate.loc[tb_pos_neg_rate['country'] == "Kenya", ['e_inc_num','year']]
box_plot_ug = tb_pos_neg_rate.loc[tb_pos_neg_rate['country'] == "Uganda", ['e_inc_num', 'year']]
#combined dataset
combine_dataset = pd.merge(box_plot_kenya, box_plot_ug, on = ['year'], how = 'inner')
#Rename series
combine_dataset.rename(columns = {"e_inc_num_x":"e_inc_num_Ke", "e_inc_num_y":"e_inc_num_Ug"}, inplace = True)
#drop year column
combine_dataset = combine_dataset.drop("year", axis = 1)
#plot box plot
combine_dataset.plot.box()

all_tb.loc[all_tb['country']=='Kenya',['e_inc_num']].describe().round()

all_tb.loc[all_tb['country']=='Uganda',['e_inc_num']].describe().round()


box_plot_kenya = tb_pos_neg_rate.loc[tb_pos_neg_rate['country'] == "Kenya", ['e_pop_num','year']]
box_plot_ug = tb_pos_neg_rate.loc[tb_pos_neg_rate['country'] == "Uganda", ['e_pop_num', 'year']]
#combined dataset
combine_dataset = pd.merge(box_plot_kenya, box_plot_ug, on = ['year'], how = 'inner')
#Rename series
combine_dataset.rename(columns = {"e_inc_num_x":"e_inc_num_Ke", "e_inc_num_y":"e_inc_num_Ug"}, inplace = True)
#drop year column
combine_dataset = combine_dataset.drop("year", axis = 1)
#plot box plot
combine_dataset.plot.box()

#creating population for Kenya 
pop_ke = all_tb.loc[all_tb['country']=='Kenya',['e_pop_num', 'year']]

#creating population for Uganda
pop_ug = all_tb.loc[all_tb['country']=='Uganda',['e_pop_num', 'year']]

#combine dataset
combine_ke_ug = pd.merge(pop_ke , pop_ug, on = ['year'], how = 'inner')

#rename series
combine_ke_ug.rename (columns = {"e_pop_num_x":"e_pop_num_Ke", "e_pop_num_y":"e_pop_num_Ug"},inplace = True)

#drop year coloumn
combine_ke_ug = combine_ke_ug.drop('year' , axis = 1)

#plot box plot
combine_ke_ug.plot.box()


len(all_tb.g_whoregion.unique())
