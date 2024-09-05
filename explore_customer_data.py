#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports

import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


#get current working directory

cwd = os.getcwd()

#read the csv

df = pd.read_csv(cwd + "/customer_booking.csv",  encoding="ISO-8859-1")


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.describe()


# In[8]:


df.info()


# In[9]:


per_internet = df.sales_channel.value_counts().values[0]  / df.sales_channel.count() *100
per_mobile = df.sales_channel.value_counts().values[1]  / df.sales_channel.count() *100


# In[10]:


print(f"Number of bookings done through internet: {per_internet} %")
print(f"Number of bookings done through phone call: {per_mobile} %")


# In[11]:


per_round = df.trip_type.value_counts().values[0]/ df.trip_type.count() *100
per_oneway = df.trip_type.value_counts().values[1]/ df.trip_type.count() *100
per_circle = df.trip_type.value_counts().values[2]/ df.trip_type.count() *100


# In[12]:


print(f"Percentage of round trips: {per_round} %")
print(f"Percentage of One way trips: {per_oneway} %")
print(f"Percentage of circle trips: {per_circle} %")


# In[13]:


plt.figure(figsize=(15,5))
sns.histplot(data=df, x="purchase_lead", binwidth=20,kde=True)


# In[14]:


(df.purchase_lead >600).value_counts()


# In[15]:


df[df.purchase_lead > 600]


# In[16]:


#filtering the data to have only purchase lead days less than 600 days
df = df[df.purchase_lead <600 ]


# In[17]:


plt.figure(figsize=(15,5))
sns.histplot(data=df, x="length_of_stay", binwidth=15,kde=True)


# In[22]:


(df.length_of_stay> 200).value_counts()


# In[23]:


df[df.length_of_stay> 500].booking_complete.value_counts()


# In[24]:


#filtering the data to have only length of stay days less than 500 days
df = df[df.purchase_lead <500 ]


# In[18]:


mapping = {
    "Mon" : 1,
    "Tue" : 2,
    "Wed" : 3,
    "Thu" : 4,
    "Fri" : 5,
    "Sat" : 6,
    "Sun" : 7
}

df.flight_day = df.flight_day.map(mapping)


# In[19]:


df.flight_day.value_counts()


# In[20]:


plt.figure(figsize=(15,5))
ax = df.booking_origin.value_counts()[:20].plot(kind="bar")
ax.set_xlabel("Countries")
ax.set_ylabel("Number of bookings")


# In[21]:


plt.figure(figsize=(15,5))
ax = df[df.booking_complete ==1].booking_origin.value_counts()[:20].plot(kind="bar")
ax.set_xlabel("Countries")
ax.set_ylabel("Number of complete bookings")


# In[25]:


successful_booking_per = df.booking_complete.value_counts().values[0] / len(df) * 100


# In[26]:


unsuccessful_booking_per = 100-successful_booking_per


# In[27]:


print(f"Out of 50000 booking entries only {round(unsuccessful_booking_per,2)} % bookings were successfull or complete.")


# In[28]:


df.to_csv(cwd + "/filtered_customer_booking.csv")


# In[ ]:




