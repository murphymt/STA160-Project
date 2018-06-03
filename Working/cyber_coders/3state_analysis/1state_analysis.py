import pandas as pd
import pickle
import os

wd5 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/Data'
wd6 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/Data/state_data'
os.chdir(wd5)

master_data_in = open('jobs_data.pickle', 'rb')
master_data = pickle.load(master_data_in)
master_data_in.close()

data_scientist_df_in = open('data_scientist_data.pickle', 'rb')
data_scientist_df = pickle.load(data_scientist_df_in)
data_scientist_df_in.close()

data_engineer_df_in = open('data_engineer_data.pickle', 'rb')
data_engineer_df = pickle.load(data_engineer_df_in)
data_engineer_df_in.close()

data_analyst_df_in = open('data_analyst_data.pickle', 'rb')
data_analyst_df = pickle.load(data_analyst_df_in)
data_analyst_df_in.close()

BI_df_in = open('BI_data.pickle', 'rb')
BI_df= pickle.load(BI_df_in)
BI_df_in.close()

finance_df_in = open('finance_data.pickle', 'rb')
finance_df  = pickle.load(finance_df_in)
finance_df_in.close()

product_manager_df_in = open('product_manager_data.pickle', 'rb')
product_manager_df = pickle.load(product_manager_df_in)
product_manager_df_in.close()

# count the states
USA_df = master_data.copy()
total_state_counts = pd.DataFrame()
total_state_counts['Total State Frequency'] = USA_df['States'].value_counts()
total_state_counts['States'] = total_state_counts.index
total_state_counts.reset_index(drop = True, inplace = True)
total_state_counts = total_state_counts[['States', 'Total State Frequency']]
total_state_counts = total_state_counts.reset_index(drop = True)
wd7 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/3state_analysis/total_state_frequencies'
os.chdir(wd7)
total_state_counts.to_csv('total_state_frequencies.csv', index = False)
os.chdir(wd6)
total_state_counts_out = open('total_state_counts.pickle', 'wb')
pickle.dump(total_state_counts, total_state_counts_out)
total_state_counts_out.close()

total_job_counts = pd.DataFrame()
total_job_counts['Total Job Frequency'] = USA_df['Search'].value_counts()
total_job_counts['Search'] = total_job_counts.index
total_job_counts.reset_index(drop = True, inplace = True)
total_job_counts = total_job_counts[['Search', 'Total Job Frequency']]
total_job_counts = total_job_counts.reset_index(drop = True)
wd8 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/3state_analysis/total_job_frequencies'
os.chdir(wd8)
total_job_counts.to_csv('total_job_frequencies.csv', index = False)
os.chdir(wd6)
total_job_counts_out = open('total_state_counts.pickle', 'wb')
pickle.dump(total_job_counts, total_job_counts_out)
total_job_counts_out.close()


# What are the unique states that are IN the USA
unique_states = master_data['States'].unique()

wd9 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/3state_analysis/state_city_frequencies'
wd10 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/3state_analysis/state_job_frequencies'
# California
CA_df = master_data.copy()
CA_df = CA_df[CA_df['States'].str.contains('CA')]
CA_df.reset_index(drop = True, inplace = True)
CA_city_counts = pd.DataFrame()
CA_city_counts['City Frequency'] = CA_df['Cities'].value_counts()
CA_city_counts['Cities'] = CA_city_counts.index
CA_city_counts.reset_index(drop = True, inplace = True)
CA_city_counts = CA_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
CA_city_counts.to_csv('CA_city_frequencies.csv', index = False)
os.chdir(wd6)
CA_city_counts_out = open('CA_city_counts.pickle', 'wb')
pickle.dump(CA_city_counts, CA_city_counts_out)
CA_city_counts_out.close()

CA_job_counts = pd.DataFrame()
CA_job_counts['CA Job Frequency'] = CA_df['Search'].value_counts()
CA_job_counts['Search'] = CA_job_counts.index
CA_job_counts.reset_index(drop = True, inplace = True)
CA_job_counts = CA_job_counts[['Search', 'CA Job Frequency']]
os.chdir(wd10)
CA_job_counts.to_csv('CA_job_frequencies.csv', index = False)
os.chdir(wd6)
CA_job_counts_out = open('CA_job_counts.pickle', 'wb')
pickle.dump(CA_job_counts, CA_job_counts_out)
CA_job_counts_out.close()

# Texas
TX_df = master_data.copy()
TX_df = TX_df[TX_df['States'].str.contains('TX')]
TX_df.reset_index(drop = True, inplace = True)
TX_city_counts = pd.DataFrame()
TX_city_counts['City Frequency'] = TX_df['Cities'].value_counts()
TX_city_counts['Cities'] = TX_city_counts.index
TX_city_counts.reset_index(drop = True, inplace = True)
TX_city_counts = TX_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
TX_city_counts.to_csv('TX_city_frequencies.csv', index = False)
os.chdir(wd6)
TX_city_counts_out = open('TX_city_counts.pickle', 'wb')
pickle.dump(TX_city_counts, TX_city_counts_out)
TX_city_counts_out.close()

TX_job_counts = pd.DataFrame()
TX_job_counts['TX Job Frequency'] = TX_df['Search'].value_counts()
TX_job_counts['Search'] = TX_job_counts.index
TX_job_counts.reset_index(drop = True, inplace = True)
TX_job_counts = TX_job_counts[['Search', 'TX Job Frequency']]
os.chdir(wd10)
TX_job_counts.to_csv('TX_job_frequencies.csv', index = False)
os.chdir(wd6)
TX_job_counts_out = open('TX_job_counts.pickle', 'wb')
pickle.dump(TX_job_counts, TX_job_counts_out)
TX_job_counts_out.close()

# Massassachusetts
MA_df = master_data.copy()
MA_df = MA_df[MA_df['States'].str.contains('MA')]
MA_df.reset_index(drop = True, inplace = True)
MA_city_counts = pd.DataFrame()
MA_city_counts['City Frequency'] = MA_df['Cities'].value_counts()
MA_city_counts['Cities'] = MA_city_counts.index
MA_city_counts.reset_index(drop = True, inplace = True)
MA_city_counts = MA_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
MA_city_counts.to_csv('MA_city_frequencies.csv', index = False)
os.chdir(wd6)
MA_city_counts_out = open('MA_city_counts.pickle', 'wb')
pickle.dump(MA_city_counts, MA_city_counts_out)
MA_city_counts_out.close()

MA_job_counts = pd.DataFrame()
MA_job_counts['MA Job Frequency'] = MA_df['Search'].value_counts()
MA_job_counts['Search'] = MA_job_counts.index
MA_job_counts.reset_index(drop = True, inplace = True)
MA_job_counts = MA_job_counts[['Search', 'MA Job Frequency']]
os.chdir(wd10)
MA_job_counts.to_csv('MA_job_frequencies.csv', index = False)
os.chdir(wd6)
MA_job_counts_out = open('MA_job_counts.pickle', 'wb')
pickle.dump(MA_job_counts, MA_job_counts_out)
MA_job_counts_out.close()

# Maryland
MD_df = master_data.copy()
MD_df = MD_df[MD_df['States'].str.contains('MD')]
MD_df.reset_index(drop = True, inplace = True)
MD_city_counts = pd.DataFrame()
MD_city_counts['City Frequency'] = MD_df['Cities'].value_counts()
MD_city_counts['Cities'] = MD_city_counts.index
MD_city_counts.reset_index(drop = True, inplace = True)
MD_city_counts = MD_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
MD_city_counts.to_csv('MA_city_frequencies.csv', index = False)
os.chdir(wd6)
MD_city_counts_out = open('MD_city_counts.pickle', 'wb')
pickle.dump(MD_city_counts, MD_city_counts_out)
MD_city_counts_out.close()

MD_job_counts = pd.DataFrame()
MD_job_counts['MD Job Frequency'] = MD_df['Search'].value_counts()
MD_job_counts['Search'] = MD_job_counts.index
MD_job_counts.reset_index(drop = True, inplace = True)
MD_job_counts = MD_job_counts[['Search', 'MD Job Frequency']]
os.chdir(wd10)
MA_job_counts.to_csv('MA_job_frequencies.csv', index = False)
os.chdir(wd6)
MD_job_counts_out = open('MD_job_counts.pickle', 'wb')
pickle.dump(MD_job_counts, MD_job_counts_out)
MD_job_counts_out.close()

# New York
NY_df = master_data.copy()
NY_df = NY_df[NY_df['States'].str.contains('NY')]
NY_df.reset_index(drop = True, inplace = True)
NY_city_counts = pd.DataFrame()
NY_city_counts['City Frequency'] = NY_df['Cities'].value_counts()
NY_city_counts['Cities'] = NY_city_counts.index
NY_city_counts.reset_index(drop = True, inplace = True)
NY_city_counts = NY_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
NY_city_counts.to_csv('NY_city_frequencies.csv', index = False)
os.chdir(wd6)
NY_city_counts_out = open('NY_city_counts.pickle', 'wb')
pickle.dump(NY_city_counts, NY_city_counts_out)
NY_city_counts_out.close()

NY_job_counts = pd.DataFrame()
NY_job_counts['NY Job Frequency'] = NY_df['Search'].value_counts()
NY_job_counts['Search'] = NY_job_counts.index
NY_job_counts.reset_index(drop = True, inplace = True)
NY_job_counts = NY_job_counts[['Search', 'NY Job Frequency']]
os.chdir(wd10)
NY_job_counts.to_csv('NY_job_frequencies.csv', index = False)
os.chdir(wd6)
NY_job_counts_out = open('NY_job_counts.pickle', 'wb')
pickle.dump(NY_job_counts, NY_job_counts_out)
NY_job_counts_out.close()

# Pennsylvania
PA_df = master_data.copy()
PA_df = PA_df[PA_df['States'].str.contains('PA')]
PA_df.reset_index(drop = True, inplace = True)
PA_city_counts = pd.DataFrame()
PA_city_counts['City Frequency'] = PA_df['Cities'].value_counts()
PA_city_counts['Cities'] = PA_city_counts.index
PA_city_counts.reset_index(drop = True, inplace = True)
PA_city_counts = PA_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
PA_city_counts.to_csv('PA_city_frequencies.csv', index = False)
os.chdir(wd6)
PA_city_counts_out = open('PA_city_counts.pickle', 'wb')
pickle.dump(PA_city_counts, PA_city_counts_out)
PA_city_counts_out.close()

PA_job_counts = pd.DataFrame()
PA_job_counts['PA Job Frequency'] = PA_df['Search'].value_counts()
PA_job_counts['Search'] = PA_job_counts.index
PA_job_counts.reset_index(drop = True, inplace = True)
PA_job_counts = PA_job_counts[['Search', 'PA Job Frequency']]
os.chdir(wd10)
PA_job_counts.to_csv('PA_job_frequencies.csv', index = False)
os.chdir(wd6)
PA_job_counts_out = open('PA_job_counts.pickle', 'wb')
pickle.dump(PA_job_counts, PA_job_counts_out)
PA_job_counts_out.close()

# New Jersey
NJ_df = master_data.copy()
NJ_df = NJ_df[NJ_df['States'].str.contains('NJ')]
NJ_df.reset_index(drop = True, inplace = True)
NJ_city_counts = pd.DataFrame()
NJ_city_counts['City Frequency'] = NJ_df['Cities'].value_counts()
NJ_city_counts['Cities'] = NJ_city_counts.index
NJ_city_counts.reset_index(drop = True, inplace = True)
NJ_city_counts = NJ_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
NJ_city_counts.to_csv('NJ_city_frequencies.csv', index = False)
os.chdir(wd6)
NJ_city_counts_out = open('NJ_city_counts.pickle', 'wb')
pickle.dump(NJ_city_counts, NJ_city_counts_out)
NJ_city_counts_out.close()

NJ_job_counts = pd.DataFrame()
NJ_job_counts['NJ Job Frequency'] = NJ_df['Search'].value_counts()
NJ_job_counts['Search'] = NJ_job_counts.index
NJ_job_counts.reset_index(drop = True, inplace = True)
NJ_job_counts = NJ_job_counts[['Search', 'NJ Job Frequency']]
os.chdir(wd10)
NJ_job_counts.to_csv('NJ_job_frequencies.csv', index = False)
os.chdir(wd6)
NJ_job_counts_out = open('NJ_job_counts.pickle', 'wb')
pickle.dump(NJ_job_counts, NJ_job_counts_out)
NJ_job_counts_out.close()

# Illinois
IL_df = master_data.copy()
IL_df = IL_df[IL_df['States'].str.contains('IL')]
IL_df.reset_index(drop = True, inplace = True)
IL_city_counts = pd.DataFrame()
IL_city_counts['City Frequency'] = IL_df['Cities'].value_counts()
IL_city_counts['Cities'] = IL_city_counts.index
IL_city_counts.reset_index(drop = True, inplace = True)
IL_city_counts = IL_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
IL_city_counts.to_csv('IL_city_frequencies.csv', index = False)
os.chdir(wd6)
IL_city_counts_out = open('IL_city_counts.pickle', 'wb')
pickle.dump(IL_city_counts, IL_city_counts_out)
IL_city_counts_out.close()

IL_job_counts = pd.DataFrame()
IL_job_counts['IL Job Frequency'] = IL_df['Search'].value_counts()
IL_job_counts['Search'] = IL_job_counts.index
IL_job_counts.reset_index(drop = True, inplace = True)
IL_job_counts = IL_job_counts[['Search', 'IL Job Frequency']]
os.chdir(wd10)
IL_job_counts.to_csv('IL_job_frequencies.csv', index = False)
os.chdir(wd6)
IL_job_counts_out = open('IL_job_counts.pickle', 'wb')
pickle.dump(IL_job_counts, IL_job_counts_out)
IL_job_counts_out.close()

# Tennessee
TN_df = master_data.copy()
TN_df = TN_df[TN_df['States'].str.contains('TN')]
TN_df.reset_index(drop = True, inplace = True)
TN_city_counts = pd.DataFrame()
TN_city_counts['City Frequency'] = TN_df['Cities'].value_counts()
TN_city_counts['Cities'] = TN_city_counts.index
TN_city_counts.reset_index(drop = True, inplace = True)
TN_city_counts = TN_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
TN_city_counts.to_csv('TN_city_frequencies.csv', index = False)
os.chdir(wd6)
TN_city_counts_out = open('TN_city_counts.pickle', 'wb')
pickle.dump(TN_city_counts, TN_city_counts_out)
TN_city_counts_out.close()

TN_job_counts = pd.DataFrame()
TN_job_counts['TN Job Frequency'] = TN_df['Search'].value_counts()
TN_job_counts['Search'] = TN_job_counts.index
TN_job_counts.reset_index(drop = True, inplace = True)
TN_job_counts = TN_job_counts[['Search', 'TN Job Frequency']]
os.chdir(wd10)
TN_job_counts.to_csv('TN_job_frequencies.csv', index = False)
os.chdir(wd6)
TN_job_counts_out = open('TN_job_counts.pickle', 'wb')
pickle.dump(TN_job_counts, TN_job_counts_out)
TN_job_counts_out.close()

# Kansas
KS_df = master_data.copy()
KS_df = KS_df[KS_df['States'].str.contains('KS')]
KS_df.reset_index(drop = True, inplace = True)
KS_city_counts = pd.DataFrame()
KS_city_counts['City Frequency'] = KS_df['Cities'].value_counts()
KS_city_counts['Cities'] = KS_city_counts.index
KS_city_counts.reset_index(drop = True, inplace = True)
KS_city_counts = KS_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
KS_city_counts.to_csv('KS_city_frequencies.csv', index = False)
os.chdir(wd6)
KS_city_counts_out = open('KS_city_counts.pickle', 'wb')
pickle.dump(KS_city_counts, KS_city_counts_out)
KS_city_counts_out.close()

KS_job_counts = pd.DataFrame()
KS_job_counts['KS Job Frequency'] = KS_df['Search'].value_counts()
KS_job_counts['Search'] = KS_job_counts.index
KS_job_counts.reset_index(drop = True, inplace = True)
KS_job_counts = KS_job_counts[['Search', 'KS Job Frequency']]
os.chdir(wd10)
KS_job_counts.to_csv('KS_job_frequencies.csv', index = False)
os.chdir(wd6)
KS_job_counts_out = open('KS_job_counts.pickle', 'wb')
pickle.dump(KS_job_counts, KS_job_counts_out)
KS_job_counts_out.close()

# Virginia
VA_df = master_data.copy()
VA_df = VA_df[VA_df['States'].str.contains('VA')]
VA_df.reset_index(drop = True, inplace = True)
VA_city_counts = pd.DataFrame()
VA_city_counts['City Frequency'] = VA_df['Cities'].value_counts()
VA_city_counts['Cities'] = VA_city_counts.index
VA_city_counts.reset_index(drop = True, inplace = True)
VA_city_counts = VA_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
VA_city_counts.to_csv('VA_city_frequencies.csv', index = False)
os.chdir(wd6)
VA_city_counts_out = open('VA_city_counts.pickle', 'wb')
pickle.dump(VA_city_counts, VA_city_counts_out)
VA_city_counts_out.close()

VA_job_counts = pd.DataFrame()
VA_job_counts['VA Job Frequency'] = VA_df['Search'].value_counts()
VA_job_counts['Search'] = VA_job_counts.index
VA_job_counts.reset_index(drop = True, inplace = True)
VA_job_counts = VA_job_counts[['Search', 'VA Job Frequency']]
os.chdir(wd10)
VA_job_counts.to_csv('VA_job_frequencies.csv', index = False)
os.chdir(wd6)
VA_job_counts_out = open('VA_job_counts.pickle', 'wb')
pickle.dump(VA_job_counts, VA_job_counts_out)
VA_job_counts_out.close()

# North Carolina
NC_df = master_data.copy()
NC_df = NC_df[NC_df['States'].str.contains('NC')]
NC_df.reset_index(drop = True, inplace = True)
NC_city_counts = pd.DataFrame()
NC_city_counts['City Frequency'] = NC_df['Cities'].value_counts()
NC_city_counts['Cities'] = NC_city_counts.index
NC_city_counts.reset_index(drop = True, inplace = True)
NC_city_counts = NC_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
NC_city_counts.to_csv('NC_city_frequencies.csv', index = False)
os.chdir(wd6)
NC_city_counts_out = open('NC_city_counts.pickle', 'wb')
pickle.dump(NC_city_counts, NC_city_counts_out)
NC_city_counts_out.close()

NC_job_counts = pd.DataFrame()
NC_job_counts['NC Job Frequency'] = NC_df['Search'].value_counts()
NC_job_counts['Search'] = NC_job_counts.index
NC_job_counts.reset_index(drop = True, inplace = True)
NC_job_counts = NC_job_counts[['Search', 'NC Job Frequency']]
os.chdir(wd10)
NC_job_counts.to_csv('NC_job_frequencies.csv', index = False)
os.chdir(wd6)
NC_job_counts_out = open('NC_job_counts.pickle', 'wb')
pickle.dump(NC_job_counts, NC_job_counts_out)
NC_job_counts_out.close()

# Washington
WA_df = master_data.copy()
WA_df = WA_df[WA_df['States'].str.contains('WA')]
WA_df.reset_index(drop = True, inplace = True)
WA_city_counts = pd.DataFrame()
WA_city_counts['City Frequency'] = WA_df['Cities'].value_counts()
WA_city_counts['Cities'] = WA_city_counts.index
WA_city_counts.reset_index(drop = True, inplace = True)
WA_city_counts = WA_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
WA_city_counts.to_csv('WA_city_frequencies.csv', index = False)
os.chdir(wd6)
WA_city_counts_out = open('WA_city_counts.pickle', 'wb')
pickle.dump(WA_city_counts, WA_city_counts_out)
WA_city_counts_out.close()

WA_job_counts = pd.DataFrame()
WA_job_counts['WA Job Frequency'] = WA_df['Search'].value_counts()
WA_job_counts['Search'] = WA_job_counts.index
WA_job_counts.reset_index(drop = True, inplace = True)
WA_job_counts = WA_job_counts[['Search', 'WA Job Frequency']]
os.chdir(wd10)
WA_job_counts.to_csv('WA_job_frequencies.csv', index = False)
os.chdir(wd6)
WA_job_counts_out = open('WA_job_counts.pickle', 'wb')
pickle.dump(WA_job_counts, WA_job_counts_out)
WA_job_counts_out.close()

# South Carolina
SC_df = master_data.copy()
SC_df = SC_df[SC_df['States'].str.contains('SC')]
SC_df.reset_index(drop = True, inplace = True)
SC_city_counts = pd.DataFrame()
SC_city_counts['City Frequency'] = SC_df['Cities'].value_counts()
SC_city_counts['Cities'] = SC_city_counts.index
SC_city_counts.reset_index(drop = True, inplace = True)
SC_city_counts = SC_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
SC_city_counts.to_csv('SC_city_frequencies.csv', index = False)
os.chdir(wd6)
SC_city_counts_out = open('SC_city_counts.pickle', 'wb')
pickle.dump(SC_city_counts, SC_city_counts_out)
SC_city_counts_out.close()

SC_job_counts = pd.DataFrame()
SC_job_counts['SC Job Frequency'] = SC_df['Search'].value_counts()
SC_job_counts['Search'] = SC_job_counts.index
SC_job_counts.reset_index(drop = True, inplace = True)
SC_job_counts = SC_job_counts[['Search', 'SC Job Frequency']]
os.chdir(wd10)
SC_job_counts.to_csv('SC_job_frequencies.csv', index = False)
os.chdir(wd6)
SC_job_counts_out = open('SC_job_counts.pickle', 'wb')
pickle.dump(SC_job_counts, SC_job_counts_out)
SC_job_counts_out.close()

# Missouri
MO_df = master_data.copy()
MO_df = MO_df[MO_df['States'].str.contains('MO')]
MO_df.reset_index(drop = True, inplace = True)
MO_city_counts = pd.DataFrame()
MO_city_counts['City Frequency'] = MO_df['Cities'].value_counts()
MO_city_counts['Cities'] = MO_city_counts.index
MO_city_counts.reset_index(drop = True, inplace = True)
MO_city_counts = MO_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
MO_city_counts.to_csv('MO_city_frequencies.csv', index = False)
os.chdir(wd6)
MO_city_counts_out = open('MO_city_counts.pickle', 'wb')
pickle.dump(MO_city_counts, MO_city_counts_out)
MO_city_counts_out.close()

MO_job_counts = pd.DataFrame()
MO_job_counts['MO Job Frequency'] = MO_df['Search'].value_counts()
MO_job_counts['Search'] = MO_job_counts.index
MO_job_counts.reset_index(drop = True, inplace = True)
MO_job_counts = MO_job_counts[['Search', 'MO Job Frequency']]
os.chdir(wd10)
MO_job_counts.to_csv('MO_job_frequencies.csv', index = False)
os.chdir(wd6)
MO_job_counts_out = open('MO_job_counts.pickle', 'wb')
pickle.dump(MO_job_counts, MO_job_counts_out)
MO_job_counts_out.close()

# Georgia
GA_df = master_data.copy()
GA_df = GA_df[GA_df['States'].str.contains('GA')]
GA_df.reset_index(drop = True, inplace = True)
GA_city_counts = pd.DataFrame()
GA_city_counts['City Frequency'] = GA_df['Cities'].value_counts()
GA_city_counts['Cities'] = GA_city_counts.index
GA_city_counts.reset_index(drop = True, inplace = True)
GA_city_counts = GA_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
GA_city_counts.to_csv('GA_city_frequencies.csv', index = False)
os.chdir(wd6)
GA_city_counts_out = open('GA_city_counts.pickle', 'wb')
pickle.dump(GA_city_counts, GA_city_counts_out)
GA_city_counts_out.close()

GA_job_counts = pd.DataFrame()
GA_job_counts['GA Job Frequency'] = GA_df['Search'].value_counts()
GA_job_counts['Search'] = GA_job_counts.index
GA_job_counts.reset_index(drop = True, inplace = True)
GA_job_counts = GA_job_counts[['Search', 'GA Job Frequency']]
os.chdir(wd10)
GA_job_counts.to_csv('GA_job_frequencies.csv', index = False)
os.chdir(wd6)
GA_job_counts_out = open('GA_job_counts.pickle', 'wb')
pickle.dump(GA_job_counts, GA_job_counts_out)
GA_job_counts_out.close()

# Utah
UT_df = master_data.copy()
UT_df = UT_df[UT_df['States'].str.contains('UT')]
UT_df.reset_index(drop = True, inplace = True)
UT_city_counts = pd.DataFrame()
UT_city_counts['City Frequency'] = UT_df['Cities'].value_counts()
UT_city_counts['Cities'] = UT_city_counts.index
UT_city_counts.reset_index(drop = True, inplace = True)
UT_city_counts = UT_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
UT_city_counts.to_csv('UT_city_frequencies.csv', index = False)
os.chdir(wd6)
UT_city_counts_out = open('UT_city_counts.pickle', 'wb')
pickle.dump(UT_city_counts, UT_city_counts_out)
UT_city_counts_out.close()

UT_job_counts = pd.DataFrame()
UT_job_counts['UT Job Frequency'] = UT_df['Search'].value_counts()
UT_job_counts['Search'] = UT_job_counts.index
UT_job_counts.reset_index(drop = True, inplace = True)
UT_job_counts = UT_job_counts[['Search', 'UT Job Frequency']]
os.chdir(wd10)
UT_job_counts.to_csv('UT_job_frequencies.csv', index = False)
os.chdir(wd6)
UT_job_counts_out = open('UT_job_counts.pickle', 'wb')
pickle.dump(UT_job_counts, UT_job_counts_out)
UT_job_counts_out.close()

# District of Columbia
DC_df = master_data.copy()
DC_df = DC_df[DC_df['States'].str.contains('DC')]
DC_df.reset_index(drop = True, inplace = True)
DC_city_counts = pd.DataFrame()
DC_city_counts['City Frequency'] = DC_df['Cities'].value_counts()
DC_city_counts['Cities'] = DC_city_counts.index
DC_city_counts.reset_index(drop = True, inplace = True)
DC_city_counts = DC_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
DC_city_counts.to_csv('DC_city_frequencies.csv', index = False)
os.chdir(wd6)
DC_city_counts_out = open('DC_city_counts.pickle', 'wb')
pickle.dump(DC_city_counts, DC_city_counts_out)
DC_city_counts_out.close()

DC_job_counts = pd.DataFrame()
DC_job_counts['DC Job Frequency'] = DC_df['Search'].value_counts()
DC_job_counts['Search'] = DC_job_counts.index
DC_job_counts.reset_index(drop = True, inplace = True)
DC_job_counts = DC_job_counts[['Search', 'DC Job Frequency']]
os.chdir(wd10)
DC_job_counts.to_csv('DC_job_frequencies.csv', index = False)
os.chdir(wd6)
DC_job_counts_out = open('DC_job_counts.pickle', 'wb')
pickle.dump(DC_job_counts, DC_job_counts_out)
DC_job_counts_out.close()

# Indiana
IN_df = master_data.copy()
IN_df = IN_df[IN_df['States'].str.contains('IN')]
IN_df.reset_index(drop = True, inplace = True)
IN_city_counts = pd.DataFrame()
IN_city_counts['City Frequency'] = IN_df['Cities'].value_counts()
IN_city_counts['Cities'] = IN_city_counts.index
IN_city_counts.reset_index(drop = True, inplace = True)
IN_city_counts = IN_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
IN_city_counts.to_csv('IN_city_frequencies.csv', index = False)
os.chdir(wd6)
IN_city_counts_out = open('IN_city_counts.pickle', 'wb')
pickle.dump(IN_city_counts, IN_city_counts_out)
IN_city_counts_out.close()

IN_job_counts = pd.DataFrame()
IN_job_counts['IN Job Frequency'] = IN_df['Search'].value_counts()
IN_job_counts['Search'] = IN_job_counts.index
IN_job_counts.reset_index(drop = True, inplace = True)
IN_job_counts = IN_job_counts[['Search', 'IN Job Frequency']]
os.chdir(wd10)
IN_job_counts.to_csv('IN_job_frequencies.csv', index = False)
os.chdir(wd6)
IN_job_counts_out = open('IN_job_counts.pickle', 'wb')
pickle.dump(IN_job_counts, IN_job_counts_out)
IN_job_counts_out.close()

# Mississippi
MI_df = master_data.copy()
MI_df = MI_df[MI_df['States'].str.contains('MI')]
MI_df.reset_index(drop = True, inplace = True)
MI_city_counts = pd.DataFrame()
MI_city_counts['City Frequency'] = MI_df['Cities'].value_counts()
MI_city_counts['Cities'] = MI_city_counts.index
MI_city_counts.reset_index(drop = True, inplace = True)
MI_city_counts = MI_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
MI_city_counts.to_csv('MI_city_frequencies.csv', index = False)
os.chdir(wd6)
MI_city_counts_out = open('MI_city_counts.pickle', 'wb')
pickle.dump(MI_city_counts, MI_city_counts_out)
MI_city_counts_out.close()

MI_job_counts = pd.DataFrame()
MI_job_counts['MI Job Frequency'] = MI_df['Search'].value_counts()
MI_job_counts['Search'] = MI_job_counts.index
MI_job_counts.reset_index(drop = True, inplace = True)
MI_job_counts = MI_job_counts[['Search', 'MI Job Frequency']]
os.chdir(wd10)
MI_job_counts.to_csv('MI_job_frequencies.csv', index = False)
os.chdir(wd6)
MI_job_counts_out = open('MI_job_counts.pickle', 'wb')
pickle.dump(MI_job_counts, MI_job_counts_out)
MI_job_counts_out.close()

# Connecticut
CT_df = master_data.copy()
CT_df = CT_df[CT_df['States'].str.contains('CT')]
CT_df.reset_index(drop = True, inplace = True)
CT_city_counts = pd.DataFrame()
CT_city_counts['City Frequency'] = CT_df['Cities'].value_counts()
CT_city_counts['Cities'] = CT_city_counts.index
CT_city_counts.reset_index(drop = True, inplace = True)
CT_city_counts = CT_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
CT_city_counts.to_csv('CT_city_frequencies.csv', index = False)
os.chdir(wd6)
CT_city_counts_out = open('CT_city_counts.pickle', 'wb')
pickle.dump(CT_city_counts, CT_city_counts_out)
CT_city_counts_out.close()

CT_job_counts = pd.DataFrame()
CT_job_counts['CT Job Frequency'] = CT_df['Search'].value_counts()
CT_job_counts['Search'] = CT_job_counts.index
CT_job_counts.reset_index(drop = True, inplace = True)
CT_job_counts = CT_job_counts[['Search', 'CT Job Frequency']]
os.chdir(wd10)
CT_job_counts.to_csv('CT_job_frequencies.csv', index = False)
os.chdir(wd6)
CT_job_counts_out = open('CT_job_counts.pickle', 'wb')
pickle.dump(CT_job_counts, CT_job_counts_out)
CT_job_counts_out.close()

# Florida
FL_df = master_data.copy()
FL_df = FL_df[FL_df['States'].str.contains('FL')]
FL_df.reset_index(drop = True, inplace = True)
FL_city_counts = pd.DataFrame()
FL_city_counts['City Frequency'] = FL_df['Cities'].value_counts()
FL_city_counts['Cities'] = FL_city_counts.index
FL_city_counts.reset_index(drop = True, inplace = True)
FL_city_counts = FL_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
FL_city_counts.to_csv('FL_city_frequencies.csv', index = False)
os.chdir(wd6)
FL_city_counts_out = open('FL_city_counts.pickle', 'wb')
pickle.dump(FL_city_counts, FL_city_counts_out)
FL_city_counts_out.close()

FL_job_counts = pd.DataFrame()
FL_job_counts['FL Job Frequency'] = FL_df['Search'].value_counts()
FL_job_counts['Search'] = FL_job_counts.index
FL_job_counts.reset_index(drop = True, inplace = True)
FL_job_counts = FL_job_counts[['Search', 'FL Job Frequency']]
os.chdir(wd10)
FL_job_counts.to_csv('FL_job_frequencies.csv', index = False)
os.chdir(wd6)
FL_job_counts_out = open('FL_job_counts.pickle', 'wb')
pickle.dump(FL_job_counts, FL_job_counts_out)
FL_job_counts_out.close()

# Nevada
NV_df = master_data.copy()
NV_df = NV_df[NV_df['States'].str.contains('NV')]
NV_df.reset_index(drop = True, inplace = True)
NV_city_counts = pd.DataFrame()
NV_city_counts['City Frequency'] = NV_df['Cities'].value_counts()
NV_city_counts['Cities'] = NV_city_counts.index
NV_city_counts.reset_index(drop = True, inplace = True)
NV_city_counts = NV_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
NV_city_counts.to_csv('NV_city_frequencies.csv', index = False)
os.chdir(wd6)
NV_city_counts_out = open('NV_city_counts.pickle', 'wb')
pickle.dump(NV_city_counts, NV_city_counts_out)
NV_city_counts_out.close()

NV_job_counts = pd.DataFrame()
NV_job_counts['NV Job Frequency'] = NV_df['Search'].value_counts()
NV_job_counts['Search'] = NV_job_counts.index
NV_job_counts.reset_index(drop = True, inplace = True)
NV_job_counts = NV_job_counts[['Search', 'NV Job Frequency']]
os.chdir(wd10)
NV_job_counts.to_csv('NV_job_frequencies.csv', index = False)
os.chdir(wd6)
NV_job_counts_out = open('NV_job_counts.pickle', 'wb')
pickle.dump(NV_job_counts, NV_job_counts_out)
NV_job_counts_out.close()

# Alabama
AL_df = master_data.copy()
AL_df = AL_df[AL_df['States'].str.contains('AL')]
AL_df.reset_index(drop = True, inplace = True)
AL_city_counts = pd.DataFrame()
AL_city_counts['City Frequency'] = AL_df['Cities'].value_counts()
AL_city_counts['Cities'] = AL_city_counts.index
AL_city_counts.reset_index(drop = True, inplace = True)
AL_city_counts = AL_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
AL_city_counts.to_csv('AL_city_frequencies.csv', index = False)
os.chdir(wd6)
AL_city_counts_out = open('AL_city_counts.pickle', 'wb')
pickle.dump(AL_city_counts, AL_city_counts_out)
AL_city_counts_out.close()

AL_job_counts = pd.DataFrame()
AL_job_counts['AL Job Frequency'] = AL_df['Search'].value_counts()
AL_job_counts['Search'] = AL_job_counts.index
AL_job_counts.reset_index(drop = True, inplace = True)
AL_job_counts = AL_job_counts[['Search', 'AL Job Frequency']]
os.chdir(wd10)
AL_job_counts.to_csv('AL_job_frequencies.csv', index = False)
os.chdir(wd6)
AL_job_counts_out = open('AL_job_counts.pickle', 'wb')
pickle.dump(AL_job_counts, AL_job_counts_out)
AL_job_counts_out.close()

# New Hampshire
NH_df = master_data.copy()
NH_df = NH_df[NH_df['States'].str.contains('NH')]
NH_df.reset_index(drop = True, inplace = True)
NH_city_counts = pd.DataFrame()
NH_city_counts['City Frequency'] = NH_df['Cities'].value_counts()
NH_city_counts['Cities'] = NH_city_counts.index
NH_city_counts.reset_index(drop = True, inplace = True)
NH_city_counts = NH_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
NH_city_counts.to_csv('NH_city_frequencies.csv', index = False)
os.chdir(wd6)
NH_city_counts_out = open('NH_city_counts.pickle', 'wb')
pickle.dump(NH_city_counts, NH_city_counts_out)
NH_city_counts_out.close()

NH_job_counts = pd.DataFrame()
NH_job_counts['NH Job Frequency'] = NH_df['Search'].value_counts()
NH_job_counts['Search'] = NH_job_counts.index
NH_job_counts.reset_index(drop = True, inplace = True)
NH_job_counts = NH_job_counts[['Search', 'NH Job Frequency']]
os.chdir(wd10)
NH_job_counts.to_csv('NH_job_frequencies.csv', index = False)
os.chdir(wd6)
NH_job_counts_out = open('NH_job_counts.pickle', 'wb')
pickle.dump(NH_job_counts, NH_job_counts_out)
NH_job_counts_out.close()

# Colorado
CO_df = master_data.copy()
CO_df = CO_df[CO_df['States'].str.contains('CO')]
CO_df.reset_index(drop = True, inplace = True)
CO_city_counts = pd.DataFrame()
CO_city_counts['City Frequency'] = CO_df['Cities'].value_counts()
CO_city_counts['Cities'] = CO_city_counts.index
CO_city_counts.reset_index(drop = True, inplace = True)
CO_city_counts = CO_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
CO_city_counts.to_csv('CO_city_frequencies.csv', index = False)
os.chdir(wd6)
CO_city_counts_out = open('CO_city_counts.pickle', 'wb')
pickle.dump(total_state_counts, CO_city_counts_out)
CO_city_counts_out.close()

CO_job_counts = pd.DataFrame()
CO_job_counts['CO Job Frequency'] = CO_df['Search'].value_counts()
CO_job_counts['Search'] = CO_job_counts.index
CO_job_counts.reset_index(drop = True, inplace = True)
CO_job_counts = CO_job_counts[['Search', 'CO Job Frequency']]
os.chdir(wd10)
CO_job_counts.to_csv('CO_job_frequencies.csv', index = False)
os.chdir(wd6)
CO_job_counts_out = open('CO_job_counts.pickle', 'wb')
pickle.dump(CO_job_counts, CO_job_counts_out)
CO_job_counts_out.close()

# Minnesota
MN_df = master_data.copy()
MN_df = MN_df[MN_df['States'].str.contains('MN')]
MN_df.reset_index(drop = True, inplace = True)
MN_city_counts = pd.DataFrame()
MN_city_counts['City Frequency'] = MN_df['Cities'].value_counts()
MN_city_counts['Cities'] = MN_city_counts.index
MN_city_counts.reset_index(drop = True, inplace = True)
MN_city_counts = MN_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
MN_city_counts.to_csv('MN_city_frequencies.csv', index = False)
os.chdir(wd6)
MN_city_counts_out = open('MN_city_counts.pickle', 'wb')
pickle.dump(MN_city_counts, MN_city_counts_out)
MN_city_counts_out.close()

MN_job_counts = pd.DataFrame()
MN_job_counts['MN Job Frequency'] = MN_df['Search'].value_counts()
MN_job_counts['Search'] = MN_job_counts.index
MN_job_counts.reset_index(drop = True, inplace = True)
MN_job_counts = MN_job_counts[['Search', 'MN Job Frequency']]
os.chdir(wd10)
MN_job_counts.to_csv('MN_job_frequencies.csv', index = False)
os.chdir(wd6)
MN_job_counts_out = open('MN_job_counts.pickle', 'wb')
pickle.dump(MN_job_counts, MN_job_counts_out)
MN_job_counts_out.close()

# Nebraska
NE_df = master_data.copy()
NE_df = NE_df[NE_df['States'].str.contains('NE')]
NE_df.reset_index(drop = True, inplace = True)
NE_city_counts = pd.DataFrame()
NE_city_counts['City Frequency'] = NE_df['Cities'].value_counts()
NE_city_counts['Cities'] = NE_city_counts.index
NE_city_counts.reset_index(drop = True, inplace = True)
NE_city_counts = NE_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
NE_city_counts.to_csv('NE_city_frequencies.csv', index = False)
os.chdir(wd6)
NE_city_counts_out = open('NE_city_counts.pickle', 'wb')
pickle.dump(total_state_counts, NE_city_counts_out)
NE_city_counts_out.close()

NE_job_counts = pd.DataFrame()
NE_job_counts['NE Job Frequency'] = NE_df['Search'].value_counts()
NE_job_counts['Search'] = NE_job_counts.index
NE_job_counts.reset_index(drop = True, inplace = True)
NE_job_counts = NE_job_counts[['Search', 'NE Job Frequency']]
os.chdir(wd10)
NE_job_counts.to_csv('NE_job_frequencies.csv', index = False)
os.chdir(wd6)
NE_job_counts_out = open('NE_job_counts.pickle', 'wb')
pickle.dump(NE_job_counts, NE_job_counts_out)
NE_job_counts_out.close()

# Oregon
OR_df = master_data.copy()
OR_df = OR_df[OR_df['States'].str.contains('OR')]
OR_df.reset_index(drop = True, inplace = True)
OR_city_counts = pd.DataFrame()
OR_city_counts['City Frequency'] = OR_df['Cities'].value_counts()
OR_city_counts['Cities'] = OR_city_counts.index
OR_city_counts.reset_index(drop = True, inplace = True)
OR_city_counts = OR_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
OR_city_counts.to_csv('OR_city_frequencies.csv', index = False)
os.chdir(wd6)
OR_city_counts_out = open('OR_city_counts.pickle', 'wb')
pickle.dump(OR_city_counts, OR_city_counts_out)
OR_city_counts_out.close()

OR_job_counts = pd.DataFrame()
OR_job_counts['OR Job Frequency'] = OR_df['Search'].value_counts()
OR_job_counts['Search'] = OR_job_counts.index
OR_job_counts.reset_index(drop = True, inplace = True)
OR_job_counts = OR_job_counts[['Search', 'OR Job Frequency']]
os.chdir(wd10)
OR_job_counts.to_csv('OR_job_frequencies.csv', index = False)
os.chdir(wd6)
OR_job_counts_out = open('OR_job_counts.pickle', 'wb')
pickle.dump(OR_job_counts, OR_job_counts_out)
OR_job_counts_out.close()

# Rhode Island
RI_df = master_data.copy()
RI_df = RI_df[RI_df['States'].str.contains('RI')]
RI_df.reset_index(drop = True, inplace = True)
RI_city_counts = pd.DataFrame()
RI_city_counts['City Frequency'] = RI_df['Cities'].value_counts()
RI_city_counts['Cities'] = RI_city_counts.index
RI_city_counts.reset_index(drop = True, inplace = True)
RI_city_counts = RI_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
RI_city_counts.to_csv('RI_city_frequencies.csv', index = False)
os.chdir(wd6)
RI_city_counts_out = open('RI_city_counts.pickle', 'wb')
pickle.dump(RI_city_counts, RI_city_counts_out)
RI_city_counts_out.close()

RI_job_counts = pd.DataFrame()
RI_job_counts['RI Job Frequency'] = RI_df['Search'].value_counts()
RI_job_counts['Search'] = RI_job_counts.index
RI_job_counts.reset_index(drop = True, inplace = True)
RI_job_counts = RI_job_counts[['Search', 'RI Job Frequency']]
os.chdir(wd10)
RI_job_counts.to_csv('RI_job_frequencies.csv', index = False)
os.chdir(wd6)
RI_job_counts_out = open('RI_job_counts.pickle', 'wb')
pickle.dump(RI_job_counts, RI_job_counts_out)
RI_job_counts_out.close()

# Arizona
AZ_df = master_data.copy()
AZ_df = AZ_df[AZ_df['States'].str.contains('AZ')]
AZ_df.reset_index(drop = True, inplace = True)
AZ_city_counts = pd.DataFrame()
AZ_city_counts['City Frequency'] = AZ_df['Cities'].value_counts()
AZ_city_counts['Cities'] = AZ_city_counts.index
AZ_city_counts.reset_index(drop = True, inplace = True)
AZ_city_counts = AZ_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
AZ_city_counts.to_csv('AZ_city_frequencies.csv', index = False)
os.chdir(wd6)
AZ_city_counts_out = open('AZ_city_counts.pickle', 'wb')
pickle.dump(AZ_city_counts, AZ_city_counts_out)
AZ_city_counts_out.close()

AZ_job_counts = pd.DataFrame()
AZ_job_counts['AZ Job Frequency'] = AZ_df['Search'].value_counts()
AZ_job_counts['Search'] = AZ_job_counts.index
AZ_job_counts.reset_index(drop = True, inplace = True)
AZ_job_counts = AZ_job_counts[['Search', 'AZ Job Frequency']]
os.chdir(wd10)
AZ_job_counts.to_csv('AZ_job_frequencies.csv', index = False)
os.chdir(wd6)
AZ_job_counts_out = open('AZ_job_counts.pickle', 'wb')
pickle.dump(AZ_job_counts, AZ_job_counts_out)
AZ_job_counts_out.close()

# Wisconsin
WI_df = master_data.copy()
WI_df = WI_df[WI_df['States'].str.contains('WI')]
WI_df.reset_index(drop = True, inplace = True)
WI_city_counts = pd.DataFrame()
WI_city_counts['City Frequency'] = WI_df['Cities'].value_counts()
WI_city_counts['Cities'] = WI_city_counts.index
WI_city_counts.reset_index(drop = True, inplace = True)
WI_city_counts = WI_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
WI_city_counts.to_csv('WI_city_frequencies.csv', index = False)
os.chdir(wd6)
WI_city_counts_out = open('WI_city_counts.pickle', 'wb')
pickle.dump(WI_city_counts, WI_city_counts_out)
WI_city_counts_out.close()

WI_job_counts = pd.DataFrame()
WI_job_counts['WI Job Frequency'] = WI_df['Search'].value_counts()
WI_job_counts['Search'] = WI_job_counts.index
WI_job_counts.reset_index(drop = True, inplace = True)
WI_job_counts = WI_job_counts[['Search', 'WI Job Frequency']]
os.chdir(wd10)
WI_job_counts.to_csv('WI_job_frequencies.csv', index = False)
os.chdir(wd6)
WI_job_counts_out = open('WI_job_counts.pickle', 'wb')
pickle.dump(WI_job_counts, WI_job_counts_out)
WI_job_counts_out.close()

# Louisiana 
LA_df = master_data.copy()
LA_df = LA_df[LA_df['States'].str.contains('LA')]
LA_df.reset_index(drop = True, inplace = True)
LA_city_counts = pd.DataFrame()
LA_city_counts['City Frequency'] = LA_df['Cities'].value_counts()
LA_city_counts['Cities'] = LA_city_counts.index
LA_city_counts.reset_index(drop = True, inplace = True)
LA_city_counts = LA_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
LA_city_counts.to_csv('LA_city_frequencies.csv', index = False)
os.chdir(wd6)
LA_city_counts_out = open('LA_city_counts.pickle', 'wb')
pickle.dump(LA_city_counts, LA_city_counts_out)
LA_city_counts_out.close()

LA_job_counts = pd.DataFrame()
LA_job_counts['LA Job Frequency'] = LA_df['Search'].value_counts()
LA_job_counts['Search'] = LA_job_counts.index
LA_job_counts.reset_index(drop = True, inplace = True)
LA_job_counts = LA_job_counts[['Search', 'LA Job Frequency']]
os.chdir(wd10)
LA_job_counts.to_csv('LA_job_frequencies.csv', index = False)
os.chdir(wd6)
LA_job_counts_out = open('LA_job_counts.pickle', 'wb')
pickle.dump(LA_job_counts, LA_job_counts_out)
LA_job_counts_out.close()

# Kentucky
KY_df = master_data.copy()
KY_df = KY_df[KY_df['States'].str.contains('KY')]
KY_df.reset_index(drop = True, inplace = True)
KY_city_counts = pd.DataFrame()
KY_city_counts['City Frequency'] = KY_df['Cities'].value_counts()
KY_city_counts['Cities'] = KY_city_counts.index
KY_city_counts.reset_index(drop = True, inplace = True)
KY_city_counts = KY_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
KY_city_counts.to_csv('KY_city_frequencies.csv', index = False)
os.chdir(wd6)
KY_city_counts_out = open('KY_city_counts.pickle', 'wb')
pickle.dump(KY_city_counts, KY_city_counts_out)
KY_city_counts_out.close()

KY_job_counts = pd.DataFrame()
KY_job_counts['KY Job Frequency'] = KY_df['Search'].value_counts()
KY_job_counts['Search'] = KY_job_counts.index
KY_job_counts.reset_index(drop = True, inplace = True)
KY_job_counts = KY_job_counts[['Search', 'KY Job Frequency']]
os.chdir(wd10)
KY_job_counts.to_csv('KY_job_frequencies.csv', index = False)
os.chdir(wd6)
KY_job_counts_out = open('KY_job_counts.pickle', 'wb')
pickle.dump(KY_job_counts, KY_job_counts_out)
KY_job_counts_out.close()

# Idaho
ID_df = master_data.copy()
ID_df = ID_df[ID_df['States'].str.contains('ID')]
ID_df.reset_index(drop = True, inplace = True)
ID_city_counts = pd.DataFrame()
ID_city_counts['City Frequency'] = ID_df['Cities'].value_counts()
ID_city_counts['Cities'] = ID_city_counts.index
ID_city_counts.reset_index(drop = True, inplace = True)
ID_city_counts = ID_city_counts[['Cities', 'City Frequency']]
os.chdir(wd9)
ID_city_counts.to_csv('ID_city_frequencies.csv', index = False)
os.chdir(wd6)
ID_city_counts_out = open('ID_city_counts.pickle', 'wb')
pickle.dump(ID_city_counts, ID_city_counts_out)
ID_city_counts_out.close()

ID_job_counts = pd.DataFrame()
ID_job_counts['ID Job Frequency'] = ID_df['Search'].value_counts()
ID_job_counts['Search'] = ID_job_counts.index
ID_job_counts.reset_index(drop = True, inplace = True)
ID_job_counts = ID_job_counts[['Search', 'ID Job Frequency']]
os.chdir(wd10)
ID_job_counts.to_csv('ID_job_frequencies.csv', index = False)
os.chdir(wd6)
ID_job_counts_out = open('ID_job_counts.pickle', 'wb')
pickle.dump(ID_job_counts, ID_job_counts_out)
ID_job_counts_out.close()

wd11 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/3state_analysis/job_city_frequencies'
os.chdir(wd11)
# Number of data scientist listings per city
ds_city_counts = pd.DataFrame()
ds = data_scientist_df.copy()
ds_city_counts['Frequency'] = ds['Location'].value_counts()
ds_city_counts['Location'] = ds_city_counts.index
ds_city_counts.reset_index(drop = True, inplace = True)
ds_city_counts = ds_city_counts[['Location', 'Frequency']]
os.chdir(wd11)
ds_city_counts.to_csv('data_scientist_city_frequencies.csv', index = False)
os.chdir(wd6)
ds_city_counts_out = open('ds_city_counts.pickle', 'wb')
pickle.dump(ds_city_counts, ds_city_counts_out)
ds_city_counts_out.close()

# Number of data engineer listings per city
de_city_counts = pd.DataFrame()
de = data_engineer_df.copy()
de_city_counts['Frequency'] = de['Location'].value_counts()
de_city_counts['Location'] = de_city_counts.index
de_city_counts.reset_index(drop = True, inplace = True)
de_city_counts = de_city_counts[['Location', 'Frequency']]
os.chdir(wd11)
de_city_counts.to_csv('data_engineer_city_frequencies.csv', index = False)
os.chdir(wd6)
de_city_counts_out = open('de_city_counts.pickle', 'wb')
pickle.dump(de_city_counts, de_city_counts_out)
de_city_counts_out.close()

# Number of data analyst listings per city
da_city_counts = pd.DataFrame()
da = data_analyst_df.copy()
da_city_counts['Frequency'] = da['Location'].value_counts()
da_city_counts['Location'] = da_city_counts.index
da_city_counts.reset_index(drop = True, inplace = True)
da_city_counts = da_city_counts[['Location', 'Frequency']]
os.chdir(wd11)
da_city_counts.to_csv('data_analyst_city_frequencies.csv', index = False)
os.chdir(wd6)
da_city_counts_out = open('da_city_counts.pickle', 'wb')
pickle.dump(da_city_counts, da_city_counts_out)
da_city_counts_out.close()

# Number of business intelligence listings per city
bi_city_counts = pd.DataFrame()
bi = BI_df.copy()
bi_city_counts['Frequency'] = bi['Location'].value_counts()
bi_city_counts['Location'] = bi_city_counts.index
bi_city_counts.reset_index(drop = True, inplace = True)
bi_city_counts = bi_city_counts[['Location', 'Frequency']]
os.chdir(wd11)
bi_city_counts.to_csv('business_intelligence_city_frequencies.csv', index = False)
os.chdir(wd6)
bi_city_counts_out = open('bi_city_counts.pickle', 'wb')
pickle.dump(bi_city_counts, bi_city_counts_out)
bi_city_counts_out.close()

# Number of finance listings per city
fi_city_counts = pd.DataFrame()
fi = finance_df.copy()
fi_city_counts['Frequency'] = fi['Location'].value_counts()
fi_city_counts['Location'] = fi_city_counts.index
fi_city_counts.reset_index(drop = True, inplace = True)
fi_city_counts = fi_city_counts[['Location', 'Frequency']]
os.chdir(wd11)
fi_city_counts.to_csv('finance_city_frequencies.csv', index = False)
os.chdir(wd6)
fi_city_counts_out = open('fi_city_counts.pickle', 'wb')
pickle.dump(fi_city_counts, fi_city_counts_out)
fi_city_counts_out.close()

# Number of product manager listings per city
pm_city_counts = pd.DataFrame()
pm = product_manager_df.copy()
pm_city_counts['Frequency'] = pm['Location'].value_counts()
pm_city_counts['Location'] = pm_city_counts.index
pm_city_counts.reset_index(drop = True, inplace = True)
pm_city_counts = pm_city_counts[['Location', 'Frequency']]
os.chdir(wd11)
pm_city_counts.to_csv('product_manager_city_frequencies.csv', index = False)
os.chdir(wd6)
pm_city_counts_out = open('pm_city_counts.pickle', 'wb')
pickle.dump(pm_city_counts, pm_city_counts_out)
pm_city_counts_out.close()





