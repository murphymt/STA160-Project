import requests
import pandas as pd
import lxml.html as html
import re
import time
import requests_cache

def scrap(key_word):
    Set = []
    total = []
    flattened = []
    for i in range(19):
        i = i+1
        url = 'https://www.cybercoders.com/search/?'
        parameters = dict(page=i,filtertype='permanent',searchterms=key_word)
        response = requests.get(url,params = parameters)
        time.sleep(1)
        tree = html.fromstring(response.content)
        titleelements=tree.xpath('//div[@class="job-title"]/a')
        total.append(titleelements)
    for sublist in total:
        for val in sublist:
            flattened.append(val)
            Set.append(key_word)
            
    Keys = []
    Titles = []
    Links = []
    locationlist = []
    wagelist = []
    detaillist = []
    preferlist = []
    
    for titletag in flattened:
        title = titletag.text_content().strip()
        link = titletag.items()[0][1]
        clickablelink = 'https://www.cybercoders.com' + link
        Titles.append(title)
        Links.append(clickablelink)
    for i in range(len(Links)):
        sublink = Links[i]
        response = requests.get(sublink)
        time.sleep(1)
        tree = html.fromstring(response.content)
        location(tree)
        wage(tree)
        jobdetail(tree)
        preferrefskills(tree)
        i = i+1
    dataframe = pd.DataFrame({'Job_Set': Set,'Job Title': Titles,'Location':locationlist, 'Job Salary':wagelist, 'Job Description':detaillist, 'Preferred Skills':preferlist, 'Links':Links},columns = ['Job_Set','Job Title','Location','Job Salary','Job Description','Preferred Skills','Links'])
    return dataframe        
                
Set = []
total = []
flattened = []
List = ['data scientist', 'data analyst','data engineer']

for sublist in total:
    for val in sublist:
        flattened.append(val)
        Set.append(item)
        
Keys = []
Titles = []
Links = []
for titletag in flattened:
    title = titletag.text_content().strip()
    link = titletag.items()[0][1]
    clickablelink = 'https://www.cybercoders.com' + link
    Titles.append(title)
    Links.append(clickablelink)
    
locationlist = []
wagelist = []
detaillist = []
preferlist = []

def location(newtree):
    loelements=newtree.xpath('//div[@class="location"]')[0]
    locationcontent = loelements.text_content().strip()
    locationlist.append(locationcontent)
    
def wage(newtree):
    waelements=newtree.xpath('//div[@class="wage"]')[0]
    wagecontent = waelements.text_content().strip()
    wagecontent = re.findall('\d+', wagecontent )
    wagelist.append(wagecontent)
    
def jobdetail(newtree):
    jdelements=newtree.xpath('//div[@class="job-details"]')[0]
    detailcontent = jdelements
    detaillist.append(detailcontent)
    
def preferrefskills(newtree):
    preferelements=newtree.xpath('//div[@class="skills-section"]')[0]
    prefercontent = preferelements.text_content().strip(' \t\n\r')
    preferlist.append(prefercontent)
    
for i in range(len(Links)):
    sublink = Links[i]
    response = requests.get(sublink)
    time.sleep(1)
    tree = html.fromstring(response.content)
    location(tree)
    wage(tree)
    jobdetail(tree)
    preferrefskills(tree)
    i = i+1

len(Set)

len(Titles)

df_columns = ['Job_Set','Job Title','Location','Job Salary','Job Description','Preferred Skills','Links']
dataframe = pd.DataFrame({'Job_Set': Set,
                          'Job Title': Titles,
                          'Location':locationlist, 
                          'Job Salary':wagelist, 
                          'Job Description':detaillist, 
                          'Preferred Skills':preferlist, 
                          'Links':Links},columns = df_columns)
    
dataframe

dataframe.to_csv('cybercoder.csv',index=False)














