#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Use the ! operator to run a shell command to install matplotlib
get_ipython().system('pip install matplotlib')


# In[4]:


get_ipython().system('pip install seaborn')


# In[5]:


#imports

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#regex
import re


# In[6]:


#create a dataframe from csv file

cwd = os.getcwd()

df = pd.read_csv(cwd+"/BA_reviews.csv", index_col=0)


# In[7]:


df.head()


# In[8]:


df['verified'] = df.reviews.str.contains("Trip Verified")


# In[9]:


df['verified']


# In[11]:


get_ipython().system('pip install nltk')


# In[13]:


import nltk

# Download the stopwords dataset
nltk.download('stopwords')


# In[15]:


import nltk
nltk.download('wordnet')


# In[16]:


#for lemmatization of words we will use nltk library
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
lemma = WordNetLemmatizer()


reviews_data = df.reviews.str.strip("✅ Trip Verified |")

#create an empty list to collect cleaned data corpus
corpus =[]

#loop through each review, remove punctuations, small case it, join it and add it to corpus
for rev in reviews_data:
    rev = re.sub('[^a-zA-Z]',' ', rev)
    rev = rev.lower()
    rev = rev.split()
    rev = [lemma.lemmatize(word) for word in rev if word not in set(stopwords.words("english"))]
    rev = " ".join(rev)
    corpus.append(rev)


# In[17]:


# add the corpus to the original dataframe

df['corpus'] = corpus


# In[18]:


df.head()


# In[19]:


df.dtypes


# In[21]:


date_str = "20th September 2023"
date_str = date_str.replace("th", "")
df['date'] = pd.to_datetime(date_str, format="%d %B %Y")


# In[22]:


# convert the date to datetime format

df.date = pd.to_datetime(df.date)


# In[23]:


df.date.head()


# In[24]:


#check for unique values
df.stars.unique()


# In[26]:


df.stars.value_counts()


# In[34]:


#check the unique values again
df.stars.unique()


# In[35]:


df.isnull().value_counts()


# In[36]:


df.country.isnull().value_counts()


# In[38]:


#drop the rows using index where the country value is null
df.drop(df[df.country.isnull() == True].index, axis=0, inplace=True)


# In[39]:


df.shape


# In[40]:


#resetting the index
df.reset_index(drop=True)


# In[41]:


# export the cleaned data

df.to_csv(cwd + "/cleaned-BA-reviews.csv")


# In[ ]:




