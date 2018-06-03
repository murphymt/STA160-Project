import pickle
import os
#import pandas as pd
#import numpy as np

from collections import Counter
import nltk
from nltk.corpus import stopwords
#from nltk.stem import WordNetLemmatizer
#import nltk
#from nltk import word_tokenize
#from nltk.util import ngrams

wd12 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/Data'
os.chdir(wd12)

jobs_df_in = open('jobs_data.pickle', 'rb')
jobs_df = pickle.load(jobs_df_in)
jobs_df_in.close()

ds_df_in = open('data_scientist_data.pickle', 'rb')
ds_df = pickle.load(ds_df_in)
ds_df_in.close()

de_df_in = open('data_engineer_data.pickle', 'rb')
de_df = pickle.load(de_df_in)
de_df_in.close()

da_df_in = open('data_analyst_data.pickle', 'rb')
da_df = pickle.load(da_df_in)
da_df_in.close()

bi_df_in = open('BI_data.pickle', 'rb')
bi_df = pickle.load(bi_df_in)
bi_df_in.close()

fi_df_in = open('finance_data.pickle', 'rb')
fi_df = pickle.load(fi_df_in)
fi_df_in.close()

pm_df_in = open('product_manager_data.pickle', 'rb')
pm_df = pickle.load(pm_df_in)
pm_df_in.close()

#programming_terms = ['javascript',
#                     'python',
#                     'java', 
#                     'ruby',
#                     'php',
#                     'c++',
#                     'css',
#                     'c#',
#                     'go',
#                     'c',
#                     'typescript',
#                     'shell',
#                     'swift',
#                     'scala',
#                     'objective-c']

#analysis = ['excel',
#            'tableau',
#            'sas', 
#            'spss', 
#            'd',
#            'd3'] 

def skill_count(job_typeDF):
    """
    (Purpose)
    
    (Arguments)
    
    (Returns)
    
    """
    job_skills = []
    removals = ["#", "&", "(", ")", ",", "-", "/", ":", "|"]
    stop_words = list(stopwords.words('english') + removals)
    
    
    for i in range(len(job_typeDF['Skills'])):
        list_count = {}
        lower_list = [word.lower() for word in job_typeDF['Skills'][i]]
        list_skills = ' '.join(lower_list)
        token = nltk.word_tokenize(list_skills)
        tokenized_list = [item for item in token if item not in stop_words]
        
        for skill in tokenized_list:
            if skill not in list_count.keys():
                list_count[skill] = 1    
            else:
                list_count[skill] += 1
        job_skills.append(list_count)
        i += 1
    
    
    flatten_skills = Counter()
    for dictionary in job_skills:
       for key, value in dictionary.items():
          flatten_skills[key] += value 
    flatten_skills = flatten_skills.most_common()


    return flatten_skills

# What are the most in-demand skills for each search term?
total_skillFreq = skill_count(jobs_df)
ds_skillFreq = skill_count(ds_df)
de_skillFreq = skill_count(de_df)
da_skillFreq = skill_count(da_df)
bi_skillFreq = skill_count(bi_df)
fi_skillFreq = skill_count(fi_df)
pm_skillFreq = skill_count(pm_df)

# What are the most in-demand skills for each state?
wd13 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/Data/state_data'
os.chdir(wd13)
CA_df_in = open('CA_df.pickle', 'rb')
CA_df = pickle.load(CA_df_in)
CA_df_in.close()
NY_df_in = open('NY_df.pickle', 'rb')
NY_df = pickle.load(NY_df_in)
NY_df_in.close()
TX_df_in = open('TX_df.pickle', 'rb')
TX_df = pickle.load(TX_df_in)
TX_df_in.close()
MA_df_in = open('MA_df.pickle', 'rb')
MA_df = pickle.load(MA_df_in)
MA_df_in.close()
WA_df_in = open('WA_df.pickle', 'rb')
WA_df = pickle.load(WA_df_in)
WA_df_in.close()
IL_df_in = open('IL_df.pickle', 'rb')
IL_df = pickle.load(IL_df_in)
IL_df_in.close()
VA_df_in = open('VA_df.pickle', 'rb')
VA_df = pickle.load(VA_df_in)
VA_df_in.close()
PA_df_in = open('PA_df.pickle', 'rb')
PA_df = pickle.load(PA_df_in)
PA_df_in.close()
NC_df_in = open('NC_df.pickle', 'rb')
NC_df = pickle.load(NC_df_in)
NC_df_in.close()
NJ_df_in = open('NJ_df.pickle', 'rb')
NJ_df = pickle.load(NJ_df_in)
NJ_df_in.close()
MD_df_in = open('MD_df.pickle', 'rb')
MD_df = pickle.load(MD_df_in)
MD_df_in.close()
MO_df_in = open('MO_df.pickle', 'rb')
MO_df = pickle.load(MO_df_in)
MO_df_in.close()
FL_df_in = open('FL_df.pickle', 'rb')
FL_df = pickle.load(FL_df_in)
FL_df_in.close()
GA_df_in = open('GA_df.pickle', 'rb')
GA_df = pickle.load(GA_df_in)
GA_df_in.close()
DC_df_in = open('DC_df.pickle', 'rb')
DC_df = pickle.load(DC_df_in)
DC_df_in.close()
NV_df_in = open('NV_df.pickle', 'rb')
NV_df = pickle.load(NV_df_in)
NV_df_in.close()
IN_df_in = open('IN_df.pickle', 'rb')
IN_df = pickle.load(IN_df_in)
IN_df_in.close()
WI_df_in = open('WI_df.pickle', 'rb')
WI_df = pickle.load(WI_df_in)
WI_df_in.close()
CO_df_in = open('CO_df.pickle', 'rb')
CO_df = pickle.load(CO_df_in)
CO_df_in.close()
AZ_df_in = open('AZ_df.pickle', 'rb')
AZ_df = pickle.load(AZ_df_in)
AZ_df_in.close()
AL_df_in = open('AL_df.pickle', 'rb')
AL_df = pickle.load(AL_df_in)
AL_df_in.close()
MN_df_in = open('MN_df.pickle', 'rb')
MN_df = pickle.load(MN_df_in)
MN_df_in.close()
MI_df_in = open('MI_df.pickle', 'rb')
MI_df = pickle.load(MI_df_in)
MI_df_in.close()
OH_df_in = open('OH_df.pickle', 'rb')
OH_df = pickle.load(OH_df_in)
OH_df_in.close()
SC_df_in = open('SC_df.pickle', 'rb')
SC_df = pickle.load(SC_df_in)
SC_df_in.close()
UT_df_in = open('UT_df.pickle', 'rb')
UT_df = pickle.load(UT_df_in)
UT_df_in.close()
CT_df_in = open('CT_df.pickle', 'rb')
CT_df = pickle.load(CT_df_in)
CT_df_in.close()
TN_df_in = open('TN_df.pickle', 'rb')
TN_df = pickle.load(TN_df_in)
TN_df_in.close()
LA_df_in = open('LA_df.pickle', 'rb')
LA_df = pickle.load(LA_df_in)
LA_df_in.close()
NH_df_in = open('NH_df.pickle', 'rb')
NH_df = pickle.load(NH_df_in)
NH_df_in.close()
KS_df_in = open('KS_df.pickle', 'rb')
KS_df = pickle.load(KS_df_in)
KS_df_in.close()
OR_df_in = open('OR_df.pickle', 'rb')
OR_df = pickle.load(OR_df_in)
OR_df_in.close()
RI_df_in = open('RI_df.pickle', 'rb')
RI_df = pickle.load(RI_df_in)
RI_df_in.close()
NE_df_in = open('NE_df.pickle', 'rb')
NE_df = pickle.load(NE_df_in)
NE_df_in.close()
ID_df_in = open('ID_df.pickle', 'rb')
ID_df = pickle.load(ID_df_in)
ID_df_in.close()
KY_df_in = open('KY_df.pickle', 'rb')
KY_df = pickle.load(KY_df_in)
KY_df_in.close()

# What are the most in-demand skills for each city?



# What are the most in-demand skills for each job?



# What skills are similar between pairwise search terms?
# DS:DE | DS:DA | DS:BI | DS:FI | DS:PM
# DE:DA | DE:BI | DE:FI | DE:PM
# DA:BI | DA:FI | DA:PM
# BI:FI | BI:PM
# FI:PM



# What skills are unique to each job?



# What skills differentiate data scientists, data engineers, data analysts, and business intelligence?







