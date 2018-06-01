import pandas as pd
import requests
import os
import re

wd2 = "/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/1data_collection"
os.chdir(wd2)

jobs_scrub = pd.read_csv('raw_jobs_data.csv')

jobs_scrub.columns = ['Search', 'Title', 'Location', 'Salary', 'Description', 'Skills', 'URL']

wd3 = "/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/2data_wrangling"
os.chdir(wd3)

def description_scrub(jobs_scrub, field):
    """
    (Purpose)
    Cleans up the description for each listing. The raw data has '*', '\r', \n', and 
    'Applicants must be authorized to work in the U.S.' that need to be removed in order 
    to have a cleaner format. 
    
    (Arguments)
    field : Description
        
    (Returns)
    description : list of scrubbed descriptions
    
    """
    nrows, ncols = jobs_scrub.shape
    
    removals = ['*','\r','\n','Applicants must be authorized to work in the U.S.']
    for i in range(nrows):
        for j in removals:
            jobs_scrub[field][i] = jobs_scrub[field][i].replace(j,'')
    return jobs_scrub[field]

def skills_clean(jobs_scrub, field):
    """
    (Purpose)
    Cleans up the skills for each listing. The raw data has 'Preferred Skills', '\r', and \n'
    that need to be removed in order to have a cleaner format. 
    
    (Arguments)
    field : Skills
    
    (Returns)
    skills : list of scrubbed skills
    
    """
    nrows, ncols = jobs_scrub.shape
    
    removals = ['Preferred Skills', '\r', '\n']
    for i in range(nrows):
        for j in removals:
            jobs_scrub[field][i] = jobs_scrub[field][i].replace(j,'')
        jobs_scrub[field][i] = jobs_scrub[field][i].split('  ')
    
    for i in range(nrows):
        jobs_scrub[field][i] = list(filter(None, jobs_scrub[field][i]))
    return jobs_scrub[field]

def geo_cords(jobs_scrub, field):
    
    longitude = []
    latitude = []
    
    nrows, ncols = jobs_scrub.shape
    
    for i in range(nrows):
        address = jobs_scrub[field][i]
        api_key = "AIzaSyA_bzUIipMaoeuqNQkm_62YaVK-YZgOKFc"
        api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()
        i +=1
        if api_response_dict['status'] == 'OK':
            lon = api_response_dict['results'][0]['geometry']['location']['lng']
            lat = api_response_dict['results'][0]['geometry']['location']['lat']
            
            longitude.append(lon)
            latitude.append(lat)
    
    return longitude, latitude

def location_clean(jobs_scrub, field):
    """
    (Purpose)
    Seperates the locations for each listing into city and states, which is a cleaner format for
    conducting analysis later on. 
    
    (Arguments)
    field : Location
    
    (Return)
    city : list of cities for job listings
    state : list of state for job listings
    
    """
    nrows, ncols = jobs_scrub.shape
    cities = []
    states = []
    for i in range(nrows):
        location_split = jobs_scrub[field][i].split(', ')
        cities.append(location_split[0])
        states.append(location_split[1])
    return cities, states

def salary_clean(jobs_scrub, field):
    """
    (Purpose)
    Cleans up the salary portion for each listing if there is data present. Seperates the salary
    estimates into a minimum and maximum salary estimate. Also, the format is converted into thousands
    and numeric. 
    
    (Arguments)
    field : Salary
    
    (Return)
    min_salary : list of minimum salary estimates
    max_salary : list of maximum salary estimates
    
    """
    nrows, ncols = jobs_scrub.shape
    min_salary = []
    max_salary = []
    mean_salary = []
    for i in range(nrows):
        string_holder = ''.join(jobs_scrub[field][i])
        string_holder = string_holder[string_holder.find("[") + 1:string_holder.find("]")]
        string_holder = re.findall(r'\d+', string_holder)
        jobs_scrub[field][i] = string_holder
        string_holder = ''
        
    for i in range(nrows):
        for j in range(len(jobs_scrub[field][i])):
            if len(jobs_scrub[field][i][j]) >= 2:
                jobs_scrub[field][i][j] = jobs_scrub[field][i][j] + '000'
                jobs_scrub[field][i][j] = int(jobs_scrub[field][i][j])
    
    for i in range(nrows):
        if len(jobs_scrub[field][i]) == 0:
            jobs_scrub[field][i].append(0)
            jobs_scrub[field][i].append(0)
    
    for i in range(nrows):
        min_salary.append(jobs_scrub[field][i][0])
        max_salary.append(jobs_scrub[field][i][1])
        mean_salary.append((jobs_scrub[field][i][0] + jobs_scrub[field][i][1]) / 2)
        
    for i in range(nrows):
        if min_salary[i] == 0:
            min_salary[i] = 'Unknown'
        if max_salary[i] == 0:
            max_salary[i] = 'Unknown'
        if mean_salary[i] ==0:
            mean_salary[i] = 'Unknown'
            
            
    return min_salary, max_salary, mean_salary

description_list = description_scrub(jobs_scrub, 'Description')
skills_list = skills_clean(jobs_scrub, 'Skills')
geo_list = geo_cords(jobs_scrub, 'Location')
locations_list = location_clean(jobs_scrub, 'Location')
wage_list = salary_clean(jobs_scrub, 'Salary')

jobs_scrub['Description'] = description_list
jobs_scrub['Skills'] = skills_list
jobs_scrub['Cities'] = locations_list[0]
jobs_scrub['States'] = locations_list[1]
jobs_scrub['Longitude'] = geo_list[0]
jobs_scrub['Latitude'] = geo_list[1]
jobs_scrub['Min_Salary'] = wage_list[0]
jobs_scrub['Max_Salary'] = wage_list[1]
jobs_scrub['Mean_Salary'] = wage_list[2]
jobs_scrub = jobs_scrub[jobs_scrub['Description'] != '']

jobs_scrub = jobs_scrub[['Search', 
                         'Title',
                         'Location',
                         'Cities', 
                         'States', 
                         'Latitude', 
                         'Longitude', 
                         'Description', 
                         'Skills', 
                         'Min_Salary', 
                         'Max_Salary', 
                         'Mean_Salary', 
                         'URL']]

jobs_scrub.to_csv('jobs_data.csv',index = False)





