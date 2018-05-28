import pandas as pd
import numpy as np
import plotnine as gg
import seaborn as sns
from matplotlib import pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv('cybercoder_final.csv')

n = df.shape[0]

df

# 1.) KEY WORD
kw = df['KeyWord'].value_counts()
kw

(
gg.ggplot(df, gg.aes(x = "KeyWord",fill="KeyWord")) +
gg.geom_bar(stat = "count",position='stack') +
gg.labs(title = "frequency distribution table of data analyst, data engineer and data scientist", x = "KeyWord", y = "Count")
)

plt.rcParams['figure.figsize'] = (10,20)
labels = 'Data Engineer', 'Data Scientist', 'Data Analyst '
fracs = [kw[i] for i in range(len(kw))]
explode = [0.1, 0.05,0.1]
plt.axes(aspect=1)  
colors = ['lightcoral', 'lightskyblue','lightgreen']
plt.title('pie chart of data related jobs(data analyst, data scientist, data engineer)')
plt.pie(x=fracs, labels=labels, explode=explode, autopct='%9.1f %%', colors=colors,
        shadow=True, labeldistance=1.1, startangle = 90, pctdistance = 0.8)
plt.show()

# 2.) TITLE
title = df['Title'].value_counts()
title

set(df['Title'])

# 3.) LOCATION
location = df['Location'].value_counts()
loc = pd.DataFrame({'location':location.index, 'count':location.values})
loc.head()

df.loc[:,'State'] = 0
for i in range(n):
    df['State'][i] = df['Location'][i].split(',')
    df['State'][i] = df['State'][i][1]

state = df['State'].value_counts()
state = pd.DataFrame({'State':state.index, 'count':state.values})
state.head()

(
gg.ggplot(df, gg.aes(x = "State",fill="KeyWord")) +
gg.geom_bar(stat = "count",position='stack')+
gg.theme(figure_size=(10, 6),axis_text_x=gg.element_text(rotation=80))+
gg.labs(title = "state distribution of data analyst, data engineer and data scientist", x = "State", y = "Count")
)

# 4.) SKILLS
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from wordcloud import WordCloud

add_words = ['data',
             'analysis',
             'development',
             'design',
             'modeling',
             'systems',
             'analytics',
             'test',
             'management',
             'security',
             'server',
             'system',
             'engineering',
             'model',
             'structures',
             'science',
             'software',
             'algorithms',
             'testing',
             'business']

stopwords =stopwords.words("english") + add_words 

df1 = df
for i in range(n):
    df1['Skills'][i] = df['Skills'][i].replace("#",'')
    df1['Skills'][i] = df1['Skills'][i].replace("++",'plusplus')
    df1['Skills'][i] = df1['Skills'][i].replace("Machine Learning",'Machine-Learning')
    df1['Skills'][i] = df1['Skills'][i].replace("Big Data",'Big-Data')
    df1['Skills'][i] = df1['Skills'][i].replace("Tekla Structures",'Tekla-Structures')
    
set(df['Skills'])

def wordnet_pos(tag):
    """Map a Brown POS tag to a WordNet POS tag."""
    
    table = {"N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV, "J": wordnet.ADJ}
    
    # Default to a noun.
    return table.get(tag[0], wordnet.NOUN)

def newtext(text):
    '''Return a new text after the stopwords and lemmatizing'''
    blob = TextBlob(text)
    new_text = " ".join(w for w in blob.words if w.lower() not in stopwords)
    blob = TextBlob(new_text)
    tags = [wordnet_pos(x[1]) for x in blob.pos_tags]
    new_text = " ".join(x.lemmatize(t) for x, t in zip(blob.words, tags))
    blob = TextBlob(new_text)
    return new_text

def ReturnCount(text):
    '''Return a word counts dictionary'''
    new=newtext(text)
    blob = TextBlob(new)
    return blob.word_counts  

def countdata(text):
    '''
    Sort the counts of each distinct word
    input:text(string)
    output:datafrane of the word counts dictionary
    '''
    dic=ReturnCount(text)
    count=pd.DataFrame(list(dic.items()), columns=['word', 'count'])
    return count

def countsort(text):
    '''
    sort the countdata
    input:text(string)
    output:dataframe of 10 most frequent words and their counts
    '''
    df1=countdata(text)
    newdf=df1.sort_values(by='count', ascending=False).head(20)
    return newdf

def barplot(text,theme):
    '''
    input:text(string),theme like art,sports(string)
    output:barplot of the most frequent words and counts
    '''
    data=countsort(text)
    new=newtext(text)
    plt.rcParams['figure.figsize'] = (10, 10)
    sns.set(font_scale = 1.5)

    sns.set_style("whitegrid")
    fruit_bar = sns.barplot(x = "word", y = "count", data =data)
    for item in fruit_bar.get_xticklabels():
        item.set_rotation(60)
    plt.title(theme)
    fruit_bar.set(ylabel = 'Count', xlabel = 'Word')
    p=plt.show()
    return p

def wordcloud(text,theme):
    '''
    input:text(string),theme like art,sports(string)
    output:wordcloud of the text
    '''
    data=countsort(text)
    new=newtext(text)

    # Generate a word cloud image
    wordcloud = WordCloud().generate(new)

   # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(new)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title('wordcloud of '+theme)
    p=plt.show()
    return p

# ETL: Extract-Transform-Load
# AWS: Amazon Web Services

skills=' '.join([str(i) for i in df['Skills']])
countsort(skills)

# Python is the most popular
barplot(skills, 'preferred software')

wordcloud(skills, 'preferred software')

# 5.) DESCRIPTIONS
desc=' '.join([str(i) for i in df['Description']])
df1.to_csv('cybercoder_final1.csv',index=False)
























