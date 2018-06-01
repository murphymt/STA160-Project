import math
import pandas as pd

data_scientist_url = 'https://www.cybercoders.com/search/?page=1&searchterms=Data+Scientist&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'
data_engineer_url = 'https://www.cybercoders.com/search/?page=1&searchterms=Data+Engineer&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'
data_analyst_url = 'https://www.cybercoders.com/search/?page=1&searchterms=Data+Analyst&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'
business_intelligence_url = 'https://www.cybercoders.com/search/?page=1&searchterms=Business+Intelligence+&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'
finance_url = 'https://www.cybercoders.com/search/?page=1&searchterms=Finance&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'
product_manager_url = 'https://www.cybercoders.com/search/?page=1&searchterms=Product+Manager&searchlocation=&newsearch=true&originalsearch=true&sorttype=relevance'


search = [data_scientist_url, data_engineer_url, data_analyst_url, business_intelligence_url, finance_url, product_manager_url] # append base urls into a list
search_terms = ['Data Scientist', 'Data Engineer', 'Data Analyst', 'Business Intelligence', 'Finance', 'Product Manager'] # define search terms
num_pages = [int(math.ceil(84 / 20), int(math.ceil(370 / 20)), int(math.ceil(52 / 20)), int(math.ceil(61 / 20)), int(math.ceil(116 / 20)), int(math.ceil(164 / 20))] # number of pages per search term (number of results divided by 20 listings per page)


data_scientist_crawl = shell_crawler(search[0], search_terms[0], num_pages[0])
data_scientist_titles = data_scientist_crawl[0]
data_scientist_links = data_scientist_crawl[1]
data_scientist_type = data_scientist_crawl[2]

data_engineer_crawl = shell_crawler(search[1], search_terms[1], num_pages[1])
data_engineer_titles = data_engineer_crawl[0]
data_engineer_links = data_engineer_crawl[1]
data_engineer_type = data_engineer_crawl[2]

data_analyst_crawl = shell_crawler(search[2], search_terms[2], num_pages[2])
data_analyst_titles = data_analyst_crawl[0]
data_analyst_links = data_analyst_crawl[1]
data_analyst_type = data_analyst_crawl[2]

business_intelligence_crawl = shell_crawler(search[3], search_terms[3], num_pages[3])
business_intelligence_titles = business_intelligence_crawl[0]
business_intelligence_links = business_intelligence_crawl[1]
business_intelligence_type = business_intelligence_crawl[2]

finance_crawl = shell_crawler(search[4], search_terms[4], num_pages[4])
finance_titles = finance_crawl[0]
finance_links = finance_crawl[1]
finance_type = finance_crawl[2]

product_manager_crawl = shell_crawler(search[5], search_terms[5], num_pages[5])
product_manager_titles = product_manager_crawl[0]
product_manager_links = product_manager_crawl[1]
product_manager_type = product_manager_crawl[2]

job_titles_raw = data_scientist_titles + data_engineer_titles + data_analyst_titles + business_intelligence_titles + finance_titles + product_manager_titles
job_links_raw = data_scientcist_links + data_engineer_links + data_analyst_links + business_intelligence_links + finance_links + product_manager_links
job_type_raw = data_scientcist_type + data_engineer_type + data_analyst_type + business_intelligence_type + finance_type + product_manager_type

Analyst_Jobs_Count = int(math.ceil(191 / 20)) 
Analyst_Jobs = 'https://www.cybercoders.com/jobs/analyst-jobs/?page='
Automation_Engineer_Jobs_Count = int(math.ceil(221 / 20)) 
Automation_Engineer_Jobs = 'https://www.cybercoders.com/jobs/automation-engineer-jobs/?page='
Back_End_Jobs_Count = int(math.ceil(422 / 20)) 
Back_End_Jobs = 'https://www.cybercoders.com/jobs/back-end-jobs/?page='
Big_Data_Jobs_Count = int(math.ceil(167 / 20)) 
Big_Data_Jobs = 'https://www.cybercoders.com/jobs/big-data-jobs/?page='
Build_Engineer_Jobs_Count = int(math.ceil(141 / 20)) 
Build_Engineer_Jobs = 'https://www.cybercoders.com/jobs/build-engineer-jobs/?page='
Business_Analyst_Jobs_Count = int(math.ceil(42 / 20)) 
Business_Analyst_Jobs = 'https://www.cybercoders.com/jobs/business-analyst-jobs/?page='
Business_Intelligence_Jobs_Count = int(math.ceil(62 / 20)) 
Business_Intelligence_Jobs = 'https://www.cybercoders.com/jobs/business-intelligence-jobs/?page='
Consultant_Jobs_Count = int(math.ceil(64 / 20)) 
Consultant_Jobs = 'https://www.cybercoders.com/jobs/consultant-jobs/?page='
Data_Jobs_Count = int(math.ceil(714 / 20)) 
Data_Jobs = 'https://www.cybercoders.com/jobs/data-jobs/?page='
Data_Architect_Jobs_Count = int(math.ceil(78 / 20)) 
Data_Architect_Jobs =  'https://www.cybercoders.com/jobs/data-architect-jobs/?page='
Database_Jobs_Count = int(math.ceil(229 / 20)) 
Database_Jobs = 'https://www.cybercoders.com/jobs/database-jobs/?page='
Finance_Jobs_Count = int(math.ceil(115 / 20)) 
Finance_Jobs = 'https://www.cybercoders.com/jobs/finance-jobs/?page='
Hadoop_Jobs_Count = int(math.ceil(136 / 20)) 
Hadoop_Jobs = 'https://www.cybercoders.com/jobs/hadoop-jobs/?page='
IT_Jobs_Count = int(math.ceil(415 / 20)) 
IT_Jobs = 'https://www.cybercoders.com/jobs/it-jobs/?page='
Product_Engineer_Jobs_Count = int(math.ceil(140 / 20)) 
Product_Engineer_Jobs = 'https://www.cybercoders.com/jobs/product-engineer-jobs/?page='
Product_Manager_Jobs_Count = int(math.ceil(163 / 20)) 
Product_Manager_Jobs = 'https://www.cybercoders.com/jobs/product-manager-jobs/?page='
Python_Jobs_Count = int(math.ceil(893 / 20)) 
Python_Jobs = 'https://www.cybercoders.com/jobs/python-jobs/?page='
Scientist_Jobs_Count = int(math.ceil(173 / 20)) 
Scientist_Jobs = 'https://www.cybercoders.com/jobs/scientist-jobs/?page='
Software_Jobs_Count = int(math.ceil(1680 / 20)) 
Software_Jobs = 'https://www.cybercoders.com/jobs/software-jobs/?page='
SAS_Jobs_Count = int(math.ceil(18 / 20)) 
SAS_Jobs = 'https://www.cybercoders.com/jobs/sas-jobs/?page='
SQL_Jobs_Count = int(math.ceil(828 / 20)) 
SQL_Jobs = 'https://www.cybercoders.com/jobs/sql-jobs/?page='
Systems_Analyst_Jobs_Count = int(math.ceil(48 / 20)) 
Systems_Analyst_Jobs = 'https://www.cybercoders.com/jobs/systems-analyst-jobs/?page='
Systems_Engineer_Jobs_Count = int(math.ceil(480 / 20)) 
Systems_Engineer_Jobs = 'https://www.cybercoders.com/jobs/systems-engineer-jobs/?page='

job_pages_cols = ['Analyst_Jobs',
                  'Automation_Engineer_Jobs',
                  'Back_End_Jobs',
                  'Big_Data_Jobs',
                  'Build_Engineer_Jobs',
                  'Business_Analyst_Jobs',
                  'Business_Intelligence_Jobs',
                  'Consultant_Jobs',
                  'Data_Jobs',
                  'Data_Architect_Jobs',
                  'Database_Jobs',
                  'Finance_Jobs',
                  'Hadoop_Jobs',
                  'IT_Jobs',
                  'Product_Engineer_Jobs',
                  'Product_Manager_Jobs',
                  'Python_Jobs',
                  'Scientist_Jobs',
                  'Software_Jobs',
                  'SAS_Jobs',
                  'SQL_Jobs',
                  'Systems_Analyst_Jobs',
                  'Systems_Engineer_Jobs']

job_pages = [Analyst_Jobs,
             Automation_Engineer_Jobs,
             Back_End_Jobs,
             Big_Data_Jobs,
             Build_Engineer_Jobs,
             Business_Analyst_Jobs,
             Business_Intelligence_Jobs,
             Consultant_Jobs,
             Data_Jobs,
             Data_Architect_Jobs, 
             Database_Jobs, 
             Finance_Jobs,
             Hadoop_Jobs,
             IT_Jobs,
             Product_Engineer_Jobs,
             Product_Manager_Jobs,
             Python_Jobs,
             Scientist_Jobs,  
             Software_Jobs,
             SAS_Jobs,
             SQL_Jobs,
             Systems_Analyst_Jobs,
             Systems_Engineer_Jobs]

job_pages = pd.DataFrame({job_pages_cols[0] : [job_pages[0]],
                          job_pages_cols[1] : [job_pages[1]],
                          job_pages_cols[2] : [job_pages[2]],
                          job_pages_cols[3] : [job_pages[3]],
                          job_pages_cols[4] : [job_pages[4]],
                          job_pages_cols[5] : [job_pages[5]],
                          job_pages_cols[6] : [job_pages[6]],
                          job_pages_cols[7] : [job_pages[7]],
                          job_pages_cols[8] : [job_pages[8]],
                          job_pages_cols[9] : [job_pages[9]],
                          job_pages_cols[10] : [job_pages[10]],
                          job_pages_cols[11] : [job_pages[11]],
                          job_pages_cols[12] : [job_pages[12]],
                          job_pages_cols[13] : [job_pages[13]],
                          job_pages_cols[14] : [job_pages[14]],
                          job_pages_cols[15] : [job_pages[15]],
                          job_pages_cols[16] : [job_pages[16]],
                          job_pages_cols[17] : [job_pages[17]],
                          job_pages_cols[18] : [job_pages[18]],
                          job_pages_cols[19] : [job_pages[19]],
                          job_pages_cols[20] : [job_pages[20]],
                          job_pages_cols[21] : [job_pages[21]],
                          job_pages_cols[22] : [job_pages[22]]})

job_npages_cols = ['Analyst_Jobs_Count',
                    'Automation_Engineer_Jobs_Count',
                    'Back_End_Jobs_Count',
                    'Big_Data_Jobs_Count',
                    'Build_Engineer_Count',
                    'Business_Analyst_Jobs_Count',
                    'Business_Intelligence_Jobs_Count',
                    'Consultant_Jobs_Count',
                    'Data_Jobs_Count',
                    'Data_Architect_Jobs_Count', 
                    'Database_Jobs_Count', 
                    'Finance_Jobs_Count',
                    'Hadoop_Jobs_Count',
                    'IT_jobs_Count',
                    'Product_Engineer_Jobs_Count',
                    'Product_Manager_Jobs_Count',
                    'Python_Jobs_Count',
                    'Scientist_Jobs_Count',  
                    'Software_Jobs_Count',
                    'SAS_Jobs_Count',
                    'SQL_Jobs_Count',
                    'Systems_Analyst_Jobs_Count',
                    'Systems_Engineer_Jobs_Count']

job_npages = [Analyst_Jobs_Count,
              Automation_Engineer_Jobs_Count,
              Back_End_Jobs_Count,
              Big_Data_Jobs_Count,
              Build_Engineer_Jobs_Count,
              Business_Analyst_Jobs_Count,
              Business_Intelligence_Jobs_Count,
              Consultant_Jobs_Count,
              Data_Jobs_Count,
              Data_Architect_Jobs_Count,
              Database_Jobs_Count, 
              Finance_Jobs_Count,
              Hadoop_Jobs_Count,
              IT_Jobs_Count,
              Product_Engineer_Jobs_Count,
              Product_Manager_Jobs_Count,
              Python_Jobs_Count,
              Scientist_Jobs_Count,
              Software_Jobs_Count,
              SAS_Jobs_Count,
              SQL_Jobs_Count,
              Systems_Analyst_Jobs_Count,
              Systems_Engineer_Jobs_Count]

job_npages = pd.DataFrame({job_npages_cols[0] : [job_npages[0]],
                          job_npages_cols[1] : [job_npages[1]],
                          job_npages_cols[2] : [job_npages[2]],
                          job_npages_cols[3] : [job_npages[3]],
                          job_npages_cols[4] : [job_npages[4]],
                          job_npages_cols[5] : [job_npages[5]],
                          job_npages_cols[6] : [job_npages[6]],
                          job_npages_cols[7] : [job_npages[7]],
                          job_npages_cols[8] : [job_npages[8]],
                          job_npages_cols[9] : [job_npages[9]],
                          job_npages_cols[10] : [job_npages[10]],
                          job_npages_cols[11] : [job_npages[11]],
                          job_npages_cols[12] : [job_npages[12]],
                          job_npages_cols[13] : [job_npages[13]],
                          job_npages_cols[14] : [job_npages[14]],
                          job_npages_cols[15] : [job_npages[15]],
                          job_npages_cols[16] : [job_npages[16]],
                          job_npages_cols[17] : [job_npages[17]],
                          job_npages_cols[18] : [job_npages[18]],
                          job_npages_cols[19] : [job_npages[19]],
                          job_npages_cols[20] : [job_npages[20]],
                          job_npages_cols[21] : [job_npages[21]],
                          job_npages_cols[22] : [job_npages[22]]})

