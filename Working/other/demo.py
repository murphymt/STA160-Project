import requests
import pandas as pd
import lxml.html as html
#import time
import re
import os

wd = "/Users/tmm/Documents/GitHub/STA160-Project/Working/1Data_Processing/cyber_coders"
os.chdir(wd)
    
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
    
    # query each job type (data scientist, data analyst, data engineer), crawl through each page, extract (titles, links)
    job_type = []
    job_titles = []
    job_links = []
    total_response = []
    flattened_set = []
  
    for j in range(num_pages + 1):
        j = j + 1
        url = search + str(j)
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

# Analyst : 191 job, pages = 9.9 -> 10
# Data : pages = 36.95 -> 37
# Business Analyst : pages = 2.45 -> 3
# Big Data : pages = 8.7 -> 9
# Business Intellgience : pages = 3.15 -> 4
analyst_url = "https://www.cybercoders.com/jobs/analyst-jobs/?page=" # Analyst Jobs
data_url = "https://www.cybercoders.com/jobs/data-jobs/?page=" # Data Jobs
BA_url = "https://www.cybercoders.com/jobs/business-analyst-jobs/?page=" # Business Analyst Jobs
big_data_url = "https://www.cybercoders.com/jobs/big-data-jobs/?page=" # Big Data Jobs
BI_url = "https://www.cybercoders.com/jobs/business-intelligence-jobs/?page=" # Business Intelligence Jobs

search = [analyst_url, data_url, BA_url, big_data_url, BI_url] # append base urls into a list
search_terms = ['Analyst', 'Data', 'Business Analyst', 'Big Data', 'Business Intelligence'] # define search terms
num_pages = [10, 37, 3, 9, 4] # number of pages per search term (number of results divided by 20 listings per page)


analyst_crawl = shell_crawler(search[0], search_terms[0], num_pages[0])
analyst_titles = analyst_crawl[0]
analyst_links = analyst_crawl[1]
analyst_type = analyst_crawl[2]

Data_crawl = shell_crawler(search[1], search_terms[1], num_pages[1])
Data_titles = Data_crawl[0]
Data_links = Data_crawl[1]
Data_type = Data_crawl[2]

BA_crawl = shell_crawler(search[2], search_terms[2], num_pages[2])
BA_titles = BA_crawl[0]
BA_links = BA_crawl[1]
BA_type = BA_crawl[2]

BD_crawl = shell_crawler(search[3], search_terms[3], num_pages[3])
BD_titles = BD_crawl[0]
BD_links = BD_crawl[1]
BD_type = BD_crawl[2]

BI_crawl = shell_crawler(search[4], search_terms[4], num_pages[4])
BI_titles = BI_crawl[0]
BI_links = BI_crawl[1]
BI_type = BI_crawl[2]

job_titles_raw = analyst_titles + Data_titles + BA_titles + BD_titles + BI_titles
job_links_raw = analyst_links + Data_links + BA_links + BD_links + BI_links
job_type_raw = analyst_type + Data_type + BA_type + BD_type + BI_type

# create final dataframe
dcheck_cols = ['Search', 'Title', 'URL']
dcheck_df = pd.DataFrame({'Search' : job_type_raw,
                          'Title': job_titles_raw,
                          'URL' : job_links_raw}, columns = dcheck_cols) 

# drop duplicates conditioned on the URLS
dcheck_df = dcheck_df.drop_duplicates(subset = 'URL', keep = 'last')
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
        #time.sleep(0.25)
    
    return location_list, wage_list, description_list, skills_list

# using the title and links crawl through the listings and extract the key information
listing_crawl = job_crawler(job_links)
location_list = listing_crawl[0]
wage_list = listing_crawl[1]
description_list = listing_crawl[2]
skills_list = listing_crawl[3]

# create final dataframe
df_columns = ['Search', 'Title','Location','Salary','Description','Skills','URL']
jobs_df = pd.DataFrame({'Search' : job_type,
                        'Title': job_titles,
                        'Location' : location_list, 
                        'Salary' : wage_list, 
                        'Description' : description_list, 
                        'Skills' : skills_list, 
                        'URL' : job_links}, columns = df_columns) 

jobs_df.to_csv('raw_jobs_data.csv', index = False)














