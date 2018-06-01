import pandas as pd
import os

wd4 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/cyber_coders/3jobtype_subsetting'
os.chdir(wd4)

master_data = pd.read_csv('master_data.csv')
data_scientist_df = pd.read_csv('data_scientst_data.csv')
data_engineer_df = pd.read_csv('master_data.csv')
data_analyst_df = pd.read_csv('master_data.csv')
business_intelligence_df = pd.read_csv('master_data.csv')
finance_df = pd.read_csv('master_data.csv')
product_manager_df = pd.read_csv('master_data.csv')

wd5 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/cyber_coders/4state_analysis'
os.chdir(wd5)