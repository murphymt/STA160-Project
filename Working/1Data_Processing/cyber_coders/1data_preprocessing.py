import requests
import pandas as pd
import lxml.html as html
import time
import re
import os

wd = "/Users/tmm/Documents/GitHub/STA160-Project"
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
    """
    
    # query each job type (data scientist, data analyst, data engineer), crawl through each page, extract (titles, links)
    job_titles = []
    job_links = []
    total_response = []
    flattened_set = []

    for term in search:
        i = 0
        page_count = num_pages[i]
        for j in range(page_count + 1):
            j = j + 1
            url = term + str(j)
            response = requests.get(url)
            response_tree = html.fromstring(response.content)
            title_elements = response_tree.xpath('//div[@class="job-title"]/a')
            total_response.append(title_elements)
        i = i + 1
            
    for sub_response in total_response:
        for val in sub_response:
            flattened_set.append(val)
                  
    for title_tag in flattened_set:
        title = title_tag.text_content().strip()
        link = title_tag.items()[0][1]
        job_titles.append(title)
        job_links.append('https://www.cybercoders.com' + link)
        
    
    return job_titles, job_links

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
    
    for url in range(len(job_links)):
        listing = job_links[url]
        response = requests.get(listing)
        time.sleep(0.50)
        response_tree = html.fromstring(response.content)
        
        location(response_tree, location_list) # call location helper function
        wage(response_tree, wage_list) # call wage helper function
        description(response_tree, description_list) # call description helper function
        skills(response_tree, skills_list) # call skills helper funciton
        
        url = url + 1
    
    return location_list, wage_list, description_list, skills_list

# Analyst : pages = 9.9 -> 10
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

# call the initial crawl to extract titles and their corresponding links
init_crawl = shell_crawler(search, search_terms, num_pages)
job_titles = init_crawl[0]
job_links = init_crawl[1]

# using the title and links crawl through the listings and extract the key information
prim_crawl = job_crawler(job_links)
locations = prim_crawl[0]
salaries = prim_crawl[1]
descriptions = prim_crawl[2]
qualifications = prim_crawl[3]

# create final dataframe
df_columns = ['Title','Location','Salary','Description','Skills','URL']
jobs_df = pd.DataFrame({'Title': job_titles,
                        'Location' : locations, 
                        'Salary' : salaries, 
                        'Description' : descriptions, 
                        'Skills' : qualifications, 
                        'URL' : job_links}, columns = df_columns) 

# drop duplicates conditioned on the URLS
final_df = jobs_df.drop_duplicates(subset = 'URL', keep = False)
final_df.to_csv('raw_jobs_data.csv', index = False)














