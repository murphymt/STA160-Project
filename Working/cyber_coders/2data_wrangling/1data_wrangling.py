import os
import pickle

wd2 = "/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/Data"
os.chdir(wd2)

jobs_scrub_in = open('raw_jobs_data.pickle', 'rb')
jobs_scrub = pickle.load(jobs_scrub_in)


jobs_scrub.columns = ['Search','Title','Description', 'Skills', 'Location', 'Latitude', 'Longitude', 'Salary', 'URL']

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
            holder = jobs_scrub[field][i].replace(j,'')
            jobs_scrub.loc[i,field] = holder
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
    
    removals1 = ['Preferred Skills', '\r', '\n']
    for i in range(nrows):
        for j in removals1:
            holder1 = jobs_scrub[field][i].replace(j,'')
            jobs_scrub.loc[i,field] = holder1
        #jobs_scrub.loc[i,field] = jobs_scrub.loc[i,field].split('  ')
    
    skills_split = lambda jobs_scrub : jobs_scrub[field].split('  ')
    jobs_scrub[field] = jobs_scrub.apply(skills_split, axis = 1)
    
    none_removal = lambda jobs_scrub : list(filter(None, jobs_scrub[field]))
    jobs_scrub[field] = jobs_scrub.apply(none_removal, axis = 1)
    
    
    return jobs_scrub[field]

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
    #for i in range(nrows):
    #    string_holder = ''.join(jobs_scrub[field][i])
    #    string_holder = string_holder[string_holder.find("[") + 1:string_holder.find("]")]
    #    string_holder = re.findall(r'\d+', string_holder)
    #    jobs_scrub[field][i] = string_holder
    #    string_holder = ''
        
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
locations_list = location_clean(jobs_scrub, 'Location')
wage_list = salary_clean(jobs_scrub, 'Salary')

jobs_scrub['Description'] = description_list
jobs_scrub['Skills'] = skills_list
jobs_scrub['Cities'] = locations_list[0]
jobs_scrub['States'] = locations_list[1]
jobs_scrub['Min_Salary'] = wage_list[0]
jobs_scrub['Max_Salary'] = wage_list[1]
jobs_scrub['Mean_Salary'] = wage_list[2]
jobs_scrub = jobs_scrub[jobs_scrub['Description'] != '']

jobs_scrub = jobs_scrub[['Search', 
                         'Title',
                         'Description',
                         'Skills',
                         'Location',
                         'Cities', 
                         'States', 
                         'Latitude', 
                         'Longitude', 
                         'Min_Salary', 
                         'Max_Salary', 
                         'Mean_Salary', 
                         'URL']]

# copy cleaned up jobs_data
master_data = jobs_scrub.copy()

# dataframe for data scientist
data_scientist_df = master_data.copy()
data_scientist_df = data_scientist_df[data_scientist_df['Search'].str.contains('Data Scientist')]
data_scientist_df = data_scientist_df.reset_index(drop = True)

# dataframe for data engineer
data_engineer_df = master_data.copy()
data_engineer_df = data_engineer_df[data_engineer_df['Search'].str.contains('Data Engineer')]
data_engineer_df = data_engineer_df.reset_index(drop = True)

# dataframe for data analyst
data_analyst_df = master_data.copy()
data_analyst_df = data_analyst_df[data_analyst_df['Search'].str.contains('Data Analyst')]
data_analyst_df = data_analyst_df.reset_index(drop = True)

# dataframe for business intelligence
business_intelligence_df = master_data.copy()
business_intelligence_df = business_intelligence_df[business_intelligence_df['Search'].str.contains('Business Intelligence')]
business_intelligence_df = business_intelligence_df.reset_index(drop = True)

# dataframe for finance
finance_df = master_data.copy()
finance_df = finance_df[finance_df['Search'].str.contains('Finance')]
finance_df = finance_df.reset_index(drop = True)

# dataframe for product manager
product_manager_df = master_data.copy()
product_manager_df = product_manager_df[product_manager_df['Search'].str.contains('Product Manager')]
product_manager_df = product_manager_df.reset_index(drop = True)


master_data.to_csv('jobs_data.csv',index = False)
data_scientist_df.to_csv('data_scientist_data.csv', index = False)
data_engineer_df.to_csv('data_engineer_data.csv', index = False)
data_analyst_df.to_csv('data_analyst_data.csv', index = False)
business_intelligence_df.to_csv('BI_data.csv', index = False)
finance_df.to_csv('finance_data.csv', index = False)
product_manager_df.to_csv('product_manager_data.csv', index = False)

w4 = '/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/Data'
os.chdir(w4)

master_data_out = open('jobs_data.pickle', 'wb')
pickle.dump(master_data, master_data_out)
master_data_out.close()

data_scientist_out = open('data_scientist_data.pickle', 'wb')
pickle.dump(data_scientist_df, data_scientist_out)
data_scientist_out.close()

data_engineer_out = open('data_engineer_data.pickle', 'wb')
pickle.dump(data_engineer_df, data_engineer_out)
data_engineer_out.close()

data_analyst_out = open('data_analyst_data.pickle', 'wb')
pickle.dump(data_analyst_df, data_analyst_out)
data_analyst_out.close()

BI_out = open('BI_data.pickle', 'wb')
pickle.dump(business_intelligence_df, BI_out)
BI_out.close()

finance_out = open('finance_data.pickle', 'wb')
pickle.dump(finance_df, finance_out)
finance_out.close()

product_manager_out = open('product_manager_data.pickle', 'wb')
pickle.dump(product_manager_df, product_manager_out)
product_manager_out.close()


