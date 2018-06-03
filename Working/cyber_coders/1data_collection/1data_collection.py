import requests
import pandas as pd
import lxml.html as html
#import time
import re
import os
import math
import pickle

wd1 = "/Users/tmm/Documents/GitHub/STA160-Project/Working/cyber_coders/Data"
os.chdir(wd1)
    
def shell_crawler(search, search_terms, num_pages):
    """
    (Purpose)
    Primary crawling function that search key job terms on the cybercoders webpage and extracts
    all of the job titles and their corresponding urls. This is done so that each of the listings
    on each page of the search terms are known and then helper functions may be used to crawl through
    each one and retrieve the relevant information. 
    
    (Arguments)
    search : list of broad data/statistics related search terms to request from the the main webpage
    search_terms : list of the specific terms for each search
    num_pages : list of number of pages give each search term
    
    (Returns)
    job_titles : list of the job titles corresponding to each listing of the search results
    job_links : list of the urls corresponsing to each listing of the search results
    job_type : the "statistics" related search terms that were "techinically" inputted into the cybercoder search box

    """
    
    # query each job type (data scientist, data engineer, data analyst, business intelligence, finance, product manager ), 
    # crawl through each page, extract (titles, links, search term used)
    job_type = []
    job_titles = []
    job_links = []
    total_response = []
    flattened_set = []
  
    for j in range(num_pages + 1):
        j = j + 1
        url = search + '&page=' + str(j)
        response = requests.get(url)
        response_tree = html.fromstring(response.content)
        title_elements = response_tree.xpath('//div[@class="job-title"]/a')
        total_response.append(title_elements)
        
    for sub_response in total_response:
        for val in sub_response:
            flattened_set.append(val)
                  
    for title_tag in flattened_set:
        title = title_tag.text_content().strip()
        link = title_tag.items()[0][1]
        job_titles.append(title)
        job_links.append('https://www.cybercoders.com' + link)
        job_type.append(search_terms)
        
    return job_titles, job_links, job_type

data_scientist_url = 'https://www.cybercoders.com/search/?searchterms=Data+Scientist&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'
data_engineer_url = 'https://www.cybercoders.com/search/?searchterms=Data+Engineer&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'
data_analyst_url = 'https://www.cybercoders.com/search/?searchterms=Data+Analyst&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'
business_intelligence_url = 'https://www.cybercoders.com/search/?searchterms=Business+Intelligence+&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'
finance_url = 'https://www.cybercoders.com/search/?searchterms=Finance&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'
product_manager_url = 'https://www.cybercoders.com/search/?searchterms=Product+Manager&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'


search = [data_scientist_url, data_engineer_url, data_analyst_url, business_intelligence_url, finance_url, product_manager_url] # append base urls into a list
search_terms = ['Data Scientist', 'Data Engineer', 'Data Analyst', 'Business Intelligence', 'Finance', 'Product Manager'] # define search terms

# the number of search results divided by 20 listings per pages which is equal to the number of pages and then round up
# adjust the numerator is needed
num_pages = [int(math.ceil(84 / 20)), int(math.ceil(370 / 20)), int(math.ceil(52 / 20)), int(math.ceil(61 / 20)), int(math.ceil(116 / 20)), int(math.ceil(164 / 20))] # number of pages per search term (number of results divided by 20 listings per page)

# DATA SCIENTIST DROP DUPLICATES
data_scientist_crawl = shell_crawler(search[0], search_terms[0], num_pages[0])
data_scientist_titles = data_scientist_crawl[0]
data_scientist_links = data_scientist_crawl[1]
data_scientist_type = data_scientist_crawl[2]
ds_check_cols = ['Search', 'Title', 'URL']
ds_check = pd.DataFrame({'Search' : data_scientist_type,
                         'Title' : data_scientist_titles, 
                         'URL' : data_scientist_links}, columns = ds_check_cols)

ds_check = ds_check.drop_duplicates(subset = 'URL', keep = False)
data_scientist_titles = list(ds_check['Title'])
data_scientist_links = list(ds_check['URL'])
data_scientist_type = list(ds_check['Search'])

# DATA ENGINEER DROP DRUPLICATES
data_engineer_crawl = shell_crawler(search[1], search_terms[1], num_pages[1])
data_engineer_titles = data_engineer_crawl[0]
data_engineer_links = data_engineer_crawl[1]
data_engineer_type = data_engineer_crawl[2]
de_check_cols = ['Search', 'Title', 'URL']
de_check = pd.DataFrame({'Search' : data_engineer_type,
                         'Title' : data_engineer_titles, 
                         'URL' : data_engineer_links}, columns = de_check_cols)

de_check = de_check.drop_duplicates(subset = 'URL', keep = False)
data_engineer_titles = list(de_check['Title'])
data_engineer_links = list(de_check['URL'])
data_engineer_type = list(de_check['Search'])

# DATA ANALYST DROP DUPLICATES
data_analyst_crawl = shell_crawler(search[2], search_terms[2], num_pages[2])
data_analyst_titles = data_analyst_crawl[0]
data_analyst_links = data_analyst_crawl[1]
data_analyst_type = data_analyst_crawl[2]
da_check_cols = ['Search', 'Title', 'URL']
da_check = pd.DataFrame({'Search' : data_analyst_type,
                         'Title' : data_analyst_titles, 
                         'URL' : data_analyst_links}, columns = da_check_cols)

da_check = da_check.drop_duplicates(subset = 'URL', keep = False)
data_analyst_titles = list(da_check['Title'])
data_analyst_links = list(da_check['URL'])
data_analyst_type = list(da_check['Search'])

# BUSINESS INTELLIGENCE DROP DUPLICATES
business_intelligence_crawl = shell_crawler(search[3], search_terms[3], num_pages[3])
business_intelligence_titles = business_intelligence_crawl[0]
business_intelligence_links = business_intelligence_crawl[1]
business_intelligence_type = business_intelligence_crawl[2]
bi_check_cols = ['Search', 'Title', 'URL']
bi_check = pd.DataFrame({'Search' : business_intelligence_type,
                         'Title' : business_intelligence_titles, 
                         'URL' : business_intelligence_links}, columns = bi_check_cols)

bi_check = bi_check.drop_duplicates(subset = 'URL', keep = False)
business_intelligence_titles = list(bi_check['Title'])
business_intelligence_links = list(bi_check['URL'])
business_intelligence_type = list(bi_check['Search'])

# FINANCE DROP DUPLICATES
finance_crawl = shell_crawler(search[4], search_terms[4], num_pages[4])
finance_titles = finance_crawl[0]
finance_links = finance_crawl[1]
finance_type = finance_crawl[2]
fi_check_cols = ['Search', 'Title', 'URL']
fi_check = pd.DataFrame({'Search' : finance_type,
                         'Title' : finance_titles, 
                         'URL' : finance_links}, columns = fi_check_cols)

fi_check = fi_check.drop_duplicates(subset = 'URL', keep = False)
finance_titles = list(fi_check['Title'])
finance_links = list(fi_check['URL'])
finance_type = list(fi_check['Search'])

# PRODUCT MANAGER DROP DUPLICATES
product_manager_crawl = shell_crawler(search[5], search_terms[5], num_pages[5])
product_manager_titles = product_manager_crawl[0]
product_manager_links = product_manager_crawl[1]
product_manager_type = product_manager_crawl[2]
pm_check_cols = ['Search', 'Title', 'URL']
pm_check = pd.DataFrame({'Search' : product_manager_type,
                         'Title' : product_manager_titles, 
                         'URL' : product_manager_links}, columns = pm_check_cols)

pm_check = pm_check.drop_duplicates(subset = 'URL', keep = False)
product_manager_titles = list(pm_check['Title'])
product_manager_links = list(pm_check['URL'])
product_manager_type = list(pm_check['Search'])


job_titles_raw = data_scientist_titles + data_engineer_titles + data_analyst_titles + business_intelligence_titles + finance_titles + product_manager_titles
job_links_raw = data_scientist_links + data_engineer_links + data_analyst_links + business_intelligence_links + finance_links + product_manager_links
job_type_raw = data_scientist_type + data_engineer_type + data_analyst_type + business_intelligence_type + finance_type + product_manager_type

# drop duplicates
dcheck_cols = ['Search', 'Title', 'URL']
dcheck_df = pd.DataFrame({'Search' : job_type_raw,
                          'Title': job_titles_raw,
                          'URL' : job_links_raw}, columns = dcheck_cols) 

# drop duplicates conditioned on the URLS
dcheck_df = dcheck_df.drop_duplicates(subset = 'URL', keep = False)
job_titles = list(dcheck_df['Title'])
job_links = list(dcheck_df['URL'])
job_type = list(dcheck_df['Search'])

def location(newtree, location_list):
    """
    (Purpose)
    Helper function for extracting the location corresponding to each job listing.
    This is called from the "job_crawler" function. 
    
    (Arguments)
    newtree : html tree for each job listing
    
    (Returns)
    location_list : list of locations for each of the listings
    """
    loelements = newtree.xpath('//div[@class="location"]')[0]
    locationcontent = loelements.text_content().strip()
    location_list.append(locationcontent)
    location_list =  ''.join(str(i) for i in location_list)

def wage(newtree, wage_list):
    """
   (Purpose)
    Helper function for extracting the wage corresponding to each job listing.
    This is called from the "job_crawler" function. 
    
    (Arguments)
    newtree : html tree for each job listing
    
    (Returns)
    wage_list : list of wages for each of the listings
    """
    waelements = newtree.xpath('//div[@class="wage"]')[0]
    wagecontent = waelements.text_content().strip()
    wagecontent = re.findall('\d+', wagecontent )
    wage_list.append(wagecontent)
    

def description(newtree, description_list):
    """
    (Purpose)
    Helper function for extracting the description corresponding to each job listing.
    This is called from the "job_crawler" function. 
    
    (Arguments)
    newtree : html tree for each job listing
    
    (Returns)
    description_list : list of descriptions for each of the listings
    """
    jdelements = newtree.xpath('//div[@class="job-details"]')[0]
    detailcontent = jdelements.text_content().strip()
    description_list.append(detailcontent)
    description_list = ''.join(str(i) for i in description_list)

def skills(newtree, skills_list):
    """
    (Purpose)
    Helper function for extracting the skills corresponding to each job listing.
    This is called from the "job_crawler" function. 
    
    (Arguments)
    newtree : html tree for each job listing
    
    (Returns)
    skills_list : list of skills required for each of the listings
    """
    preferelements = newtree.xpath('//div[@class="skills-section"]')[0]
    prefercontent = preferelements.text_content().strip(' \t\n\r')
    skills_list.append(prefercontent)
    skills_list = ''.join(str(i) for i in skills_list)

# Now have job titles on each page and their links
# Iterate through each page, crawl through each listing, and extract (location, wages, descriptions, skills)

def job_crawler(job_links):
    """
    (Purpose)
    Using the links returned from the "shell_crawler" function, this function extracts the 
    details relating to each job listing. 
    
    (Arguments)
    job_links : list of the urls corresponsing to each listing of the search results
    
    (Returns)
    location_list : list of locations for each of the listings
    wage_list : list of wages for each of the listings
    description_list : list of descriptions for each of the listings
    skills_list : list of skills required for each of the listings
    """
    
    location_list = []
    wage_list = []
    description_list = []
    skills_list = []
    
    for url in job_links:
        response = requests.get(url)
        response_tree = html.fromstring(response.content)
        
        location(response_tree, location_list) # call location helper function
        wage(response_tree, wage_list) # call wage helper function
        description(response_tree, description_list) # call description helper function
        skills(response_tree, skills_list) # call skills helper funciton
        #time.sleep(0.15)
    
    return location_list, wage_list, description_list, skills_list

def geo_cords(jobs_df, field):
    
    latitude = []
    longitude = []
    
    nrows, ncols = jobs_df.shape
    
    for i in range(nrows):
        address = jobs_df[field][i]
        api_key = "AIzaSyA_bzUIipMaoeuqNQkm_62YaVK-YZgOKFc"
        api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()
        i +=1
        if api_response_dict['status'] == 'OK':
            lat = api_response_dict['results'][0]['geometry']['location']['lat']
            lon = api_response_dict['results'][0]['geometry']['location']['lng']
            
            latitude.append(lat)
            longitude.append(lon)
    
    return latitude, longitude

# using the title and links crawl through the listings and extract the key information
listing_crawl = job_crawler(job_links)
location_list = listing_crawl[0]
wage_list = listing_crawl[1]
description_list = listing_crawl[2]
skills_list = listing_crawl[3]

# create final dataframe
df_columns = ['Search', 'Title','Location','Salary','Description','Skills','URL']
raw_jobs_data_df = pd.DataFrame({'Search' : job_type,
                                 'Title': job_titles,
                                 'Location' : location_list, 
                                 'Salary' : wage_list, 
                                 'Description' : description_list, 
                                 'Skills' : skills_list, 
                                 'URL' : job_links}, columns = df_columns)

geo_list = geo_cords(raw_jobs_data_df, 'Location')
raw_jobs_data_df['Latitude'] = geo_list[0]
raw_jobs_data_df['Longitude'] = geo_list[1]
raw_jobs_data_df = raw_jobs_data_df[['Search','Title','Description', 'Skills', 'Location', 'Latitude', 'Longitude', 'Salary', 'URL']]

raw_jobs_data_df.to_csv('raw_jobs_data.csv', index = False)


raw_jobs_out = open('raw_jobs_data.pickle', 'wb')
pickle.dump(raw_jobs_data_df, raw_jobs_out)
raw_jobs_out.close()








