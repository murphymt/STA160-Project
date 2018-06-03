import pandas as pd
import os 

wd12 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/2data_wrangling'
os.chdir(wd12)

master_jobDF = pd.read_csv('jobs_data.csv')

wd13 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/3jobtype_subsetting'
os.chdir(wd13)

master_dsDF = pd.read_csv('data_scientist_data.csv')
master_deDF = pd.read_csv('data_engineer_data.csv')
master_daDF = pd.read_csv('data_analyst_data.csv')
master_biDF = pd.read_csv('business_intelligence_data.csv')
master_fiDF = pd.read_csv('finance_data.csv')
master_pmDF = pd.read_csv('product_manager_data.csv')

