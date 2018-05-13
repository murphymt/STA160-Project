import requests_cache
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd 
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

########################################################################################################
########################################################################################################
########################################################################################################

def job_listings(url):
    """
    (Purpose)
    Extracts the job listing description, requirements, preferred skills, and salary range/benefits
    
    (Args)
    (url) : url for job listing
    
    (Returns)
    A dictionary of the listing description, requirements, preferred skills, and salary range/benefits

    """
    
    job_data = pd.DataFrame()
    for link in url:
        # request the the article
        req_url = urlopen(link)
        req_url_soup = BeautifulSoup(req_url, "lxml")
        
        try:
            try:
                title_finder = req_url_soup.select("h1.subhead")[0].text.strip()
            except:
                title_finder = ""
            
            try:
                location_finder = req_url_soup.select("div.location")[0].text.strip()
            except:
                location_finder = ""
            
            try:
                description_finder = req_url_soup.find(name = "div", attrs = {"data-section" : "1"})
                description = "".join(description_finder.text)
            except:
                description = ""
            
            try:
                duties_finder = req_url_soup.find(name = "div", attrs = {"data-section" : "5"})
                duties = "".join(duties_finder.text)
            except:
                duties = ""
            
            try:
                skills_finder = req_url_soup.find(name = "div", attrs = {"data-section" : "7"})
                skills = "".join(skills_finder.text)
            except:
                skills = ""
            
            try:
                benefits_finder = req_url_soup.find(name = "div", attrs = {"data-section" : "8"})
                benefits = "".join(benefits_finder.text)
            except:
                benefits = ""
            
            try:
                preferred_skills = req_url_soup.select("ul.skill-list")[0].text.split()
            except:
                preferred_skills = [""]

            dict_listing = {"title" : title_finder,
                            "location" : location_finder,
                            "description" : description, 
                            "responsibilties" : duties, 
                            "skills" : skills,
                            "preferred_skills" : preferred_skills,
                            "benefits" : benefits}
                            
            job_data = job_data.append(dict_listing, ignore_index = True)
        
        except:
            dict_listing = {"title" : "",
                            "location" : "",
                            "description" : "", 
                            "responsibilties" : "", 
                            "skills" : "",
                            "preferred_skills" : [""],
                            "benefits" : ""}
            job_data = job_data.append(dict_listing, ignore_index = True)
        
    return(job_data)

test = job_listings(ulinks)











