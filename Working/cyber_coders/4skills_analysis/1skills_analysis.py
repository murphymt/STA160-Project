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

total_skillFreq = skill_count(jobs_df)
ds_skillFreq = skill_count(ds_df)
de_skillFreq = skill_count(de_df)
da_skillFreq = skill_count(da_df)
bi_skillFreq = skill_count(bi_df)
fi_skillFreq = skill_count(fi_df)
pm_skillFreq = skill_count(pm_df)







