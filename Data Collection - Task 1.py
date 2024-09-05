#!/usr/bin/env python
# coding: utf-8

# In[2]:


#imports

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests 
import html5lib


# In[3]:


#create an empty list to collect all reviews
reviews  = []

#create an empty list to collect rating stars
stars = []

#create an empty list to collect date
date = []

#create an empty list to collect country the reviewer is from
country = []


# In[4]:


for i in range(1, 36):
    page = requests.get(f"https://www.airlinequality.com/airline-reviews/british-airways/page/{i}/?sortby=post_date%3ADesc&pagesize=100")
    
    soup = BeautifulSoup(page.content, "html5lib")
    
    for item in soup.find_all("div", class_="text_content"):
        reviews.append(item.text)
    
    for item in soup.find_all("div", class_ = "rating-10"):
        try:
            stars.append(item.span.text)
        except:
            print(f"Error on page {i}")
            stars.append("None")
            
    #date
    for item in soup.find_all("time"):
        date.append(item.text)
        
    #country
    for item in soup.find_all("h3"):
        country.append(item.span.next_sibling.text.strip(" ()"))


# In[5]:


#check the length of total reviews extracted
len(reviews)


# In[6]:


len(country)


# In[7]:


#check the length 
stars = stars[:3500]


# In[8]:


#create  a dataframe from these collected lists of data

df = pd.DataFrame({"reviews":reviews,"stars": stars, "date":date, "country": country})


# In[9]:


df.head()


# In[10]:


df.shape


# In[11]:


import os

cwd = os.getcwd()
df.to_csv(cwd+ "/BA_reviews.csv")


# In[ ]:




