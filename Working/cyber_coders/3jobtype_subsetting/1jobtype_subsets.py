import pandas as pd
import os

wd4 = "/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/2data_wrangling"
os.chdir(wd4)

master_data = pd.read_csv('jobs_data.csv')

wd5 = "/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/3jobtype_subsetting"
os.chdir(wd5)

data_scientist_df = master_data.copy()
data_scientist_df = data_scientist_df[data_scientist_df['Search'].str.contains('Data Scientist')]

data_engineer_df = master_data.copy()
data_engineer_df = data_engineer_df[data_engineer_df['Search'].str.contains('Data Engineer')]

data_analyst_df = master_data.copy()
data_analyst_df = data_analyst_df[data_analyst_df['Search'].str.contains('Data Analyst')]

business_intelligence_df = master_data.copy()
business_intelligence_df = business_intelligence_df[business_intelligence_df['Search'].str.contains('Business Intelligence')]

finance_df = master_data.copy()
finance_df = finance_df[finance_df['Search'].str.contains('Finance')]

product_manager_df = master_data.copy()
product_manager_df = product_manager_df[product_manager_df['Search'].str.contains('Product Manager')]

master_data.to_csv('master_data.csv',index = False)
data_scientist_df.to_csv('data_scientist_data.csv', index = False)
data_engineer_df.to_csv('data_engineer_data.csv', index = False)
data_analyst_df.to_csv('data_analyst_data.csv', index = False)
business_intelligence_df.to_csv('business_intelligence_data.csv', index = False)
finance_df.to_csv('finance_data.csv', index = False)
product_manager_df.to_csv('product_manager_data.csv', index = False)


master_data['Skills'][0]
