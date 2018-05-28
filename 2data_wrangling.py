import pandas as pd
import re

jobs_scrub = pd.read_csv('raw_jobs_data.csv')
n,m = jobs_scrub.shape

jobs_scrub.columns = ['Title', 'Location', 'Salary', 'Description', 'Skills', 'URL']

def description_scrub(field):
    lists = ['*','\r','\n','Applicants must be authorized to work in the U.S.']
    for i in range(n):
        for j in lists:
            jobs_scrub[field][i] = jobs_scrub[field][i].replace(j,'')
    return jobs_scrub[field]

def skills_clean(field):
    lists = ['Preferred Skills', '\r', '\n']
    for i in range(n):
        for j in lists:
            jobs_scrub[field][i] = jobs_scrub[field][i].replace(j,'')
        jobs_scrub[field][i] = jobs_scrub[field][i].split('  ')
    
    for i in range(len(jobs_scrub['Skills'])):
        jobs_scrub['Skills'][i] = list(filter(None, jobs_scrub['Skills'][i]))
    return jobs_scrub[field]

def location_clean(field):
    city = []
    state = []
    for i in range(len(jobs_scrub[field])):
        location_split = jobs_scrub[field][i].split(', ')
        city.append(location_split[0])
        state.append(location_split[1])
    return city, state

def salary_clean(field):
    min_salary = []
    max_salary = []
    
    for i in range(len(jobs_scrub[field])):
        string_holder = ''.join(jobs_scrub[field][i])
        string_holder = string_holder[string_holder.find("[") + 1:string_holder.find("]")]
        string_holder = re.findall(r'\d+', string_holder)
        jobs_scrub[field][i] = string_holder
        string_holder = ''
    
    for i in range(len(jobs_scrub[field])):
        if len(jobs_scrub[field][i]) == 0:
            jobs_scrub[field][i].append('')
            jobs_scrub[field][i].append('')
    
    for i in range(len(jobs_scrub[field])):
        for j in range(len(jobs_scrub[field][i])):
            if len(jobs_scrub[field][i][j]) >= 2:
                jobs_scrub[field][i][j] = jobs_scrub[field][i][j] + '000'
    
    for i in range(len(jobs_scrub[field])):
        min_salary.append(jobs_scrub[field][i][0])
        max_salary.append(jobs_scrub[field][i][1])
    
    return min_salary, max_salary

description = description_scrub('Description')
skills = skills_clean('Skills')
locations = location_clean('Location')
salaries = salary_clean('Salary')

jobs_scrub['Description'] = description
jobs_scrub['Skills'] = skills
jobs_scrub['City'] = locations[0]
jobs_scrub['State'] = locations[1]
jobs_scrub['Min_Salary'] = salaries[0]
jobs_scrub['Max_Salary'] = salaries[1]
jobs_scrub = jobs_scrub[jobs_scrub['Description'] != '']

jobs_scrub = jobs_scrub[['Title', 'City', 'State', 'Description', 'Skills', 'Min_Salary', 'Max_Salary', 'URL']]
jobs_scrub.apply(pd.to_numeric, errors = 'ignore')

jobs_scrub.to_csv('jobs_data.csv',index = False)







