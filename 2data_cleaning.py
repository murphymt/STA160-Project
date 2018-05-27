import pandas as pd
import numpy as np

df = pd.read_csv('cybercoder.csv')

df = df.drop('Unnamed: 0', 1)

n,m = df.shape
print(n,m)

df.columns = ['Title', 'Location', 'Salary', 'Description', 'Skills']

df.head()

def descrip_clean(colname):
    lists = ['*','\r','\n','Applicants must be authorized to work in the U.S.']
    for i in range(n):
        for j in lists:
            df[colname][i] = df[colname][i].replace(j,'')
    return df[colname]

def skills_clean(colname):
    for i in range(n):
        df[colname][i] = df[colname][i].replace('Preferred Skills','')
        df[colname][i] = df[colname][i].replace('     ','')
        df[colname][i] = df[colname][i].split('  ')
        length = len(df[colname][i])
        df[colname][i] = ' ,'.join(df[colname][i][2:length-3])
    return df[colname]

df['Description'] = descrip_clean('Description')
df['Skills'] = skills_clean('Skills')

# Delete duplicated data
for i in range(0,n-3):
    for j in range(i+1,n-2):
        if df['Description'][i] == df['Description'][j]:
            df['Description'][j] =''    

df = df[df['Description']!='']

n,m = df.shape
print(n,m)

df = df.drop(df.index[[2]])
df = df.reset_index(drop=True)
df.head()

df['KeyWord'] = ['Data_Scientist'] * 83 + ['Data_Analyst'] * 47 + ['Data_Engineer']*322

df = df[['KeyWord','Title', 'Location', 'Salary','Description']]

df.to_csv('cybercoder_final.csv',index=False)

