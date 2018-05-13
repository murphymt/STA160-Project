import requests_cache
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
requests_cache.install_cache("cache")

## Cybercoders.com Links
analyst_url = "https://www.cybercoders.com/jobs/analyst-jobs/?page=" # Analyst Jobs
data_url = "https://www.cybercoders.com/jobs/data-jobs/?page=" # Data Jobs
BA_url = "https://www.cybercoders.com/jobs/business-analyst-jobs/?page=" # Business Analyst Jobs
big_data_url = "https://www.cybercoders.com/jobs/big-data-jobs/?page=" # Big Data Jobs
BI_url = "https://www.cybercoders.com/jobs/business-intelligence-jobs/?page=" # Business Intelligence Jobs

def links(url, page):
    """
    (Purpose) 
    This function takes the URL for cybercoders job and the number of pages to be scraped
    and returns the URLs for the job listings on each page.

    (Args)
    (url) : url for job type , page : number of pages to be webscraped (searched manually)
    
    Job Types:
    - Analyst Jobs
    - Data Jobs
    - Business Analyst Jobs
    - Big Data Jobs
    - Business Intelligence Jobs

    (Returns)
    A list of the URLs for each article on each page of "Cybercoders"
    """
    
    job_links = []
    
    for i in range(1,page+1):
        open_url = urlopen(url + str(i))
        parse_page = BeautifulSoup(open_url, "lxml")
        content_list = parse_page.find_all(name = "div", attrs = {"class" : "job-title"})

        for j in range(len(content_list)):
            job = content_list[j].find_all("a")[0].attrs["href"]
            job_links.append("https://www.cybercoders.com" + job)
            
    return job_links

analyst_links = links(analyst_url, 10)
data_links = links(data_url, 36)
BA_links = links(BA_url, 3)
big_data_links = links(big_data_url, 8)
BI_links = links(BI_url, 4)

# total number of links extracted -> NOT UNIQUE
len(analyst_links) + len(data_links) + len(BA_links) + len(big_data_links) + len(BI_links)

ulinks = list(set(analyst_links + data_links + BA_links + big_data_links + BI_links))
len(ulinks) # total number of links extracted -> UNIQUE

def job_listings(url):
    """
    (Purpose)
    Extracts the job listing description, requirements, preferred skills, and salary range/benefits
    
    (Args)
    (url) : url for job listing
    
    (Returns)
    A dictionary of the listing description, requirements, preferred skills, and salary range/benefits

    """
    
    # request the the article
    req_url = urlopen(url)
    req_url_soup = BeautifulSoup(req_url, "lxml")
    
    
    for i in demo_job_soup.find_all(name = "div", attrs = {"class" : "job-details"}):
        if len(i.text) > 0:
            description_finder = i.find(name = "div", attrs = {"data-section" : "1"})
            description = "".join(description_finder.text)
            
            duties_finder = i.find(name = "div", attrs = {"data-section" : "5"})
            duties = "".join(duties_finder.text)
            
            skills_finder = i.find(name = "div", attrs = {"data-section" : "7"})
            skills = "".join(skills_finder.text)
            
            benefits_finder = i.find(name = "div", attrs = {"data-section" : "8"})
            benefits = "".join(benefits_finder.text)
            
            
        dict_listing = {"description" : description, 
                        "responsibilties" : duties, 
                        "skills" : skills,
                        "benefits" : benefits}
    
    return(dict_articles)

















