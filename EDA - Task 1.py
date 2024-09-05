#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install plotly')


# In[4]:


get_ipython().system('pip install wordcloud')


# In[5]:


#imports

import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import datetime as dt

from wordcloud import WordCloud, STOPWORDS


# In[6]:


# create the dataframe
cwd = os.getcwd()
df = pd.read_csv(cwd+"/cleaned-BA-reviews.csv", index_col=0)

#let's also check the index are in order
df = df.reset_index(drop=True)


# In[7]:


df.head()


# In[8]:


df.stars.mean()


# In[18]:


import matplotlib.pyplot as plt

# Create the bar chart with custom colors for the first three bars
ax = df.stars.value_counts().plot(kind="bar", figsize=(8, 6), color=['red', 'darkred', 'firebrick'] + ['dodgerblue'] * (len(df.stars.value_counts()) - 3))

# Add labels to the bars
for i, count in enumerate(df.stars.value_counts()):
    ax.text(i, count, str(count), ha="center", va="bottom")

# Add labels and title
plt.xlabel("Ratings")
plt.ylabel("Total Number of reviews with that rating")
plt.suptitle("Counts for each rating")

# Show the plot
plt.show()


# In[20]:


df_ratings


# In[21]:


df_country_review = pd.DataFrame(df.country.value_counts().head()).reset_index()


# In[22]:


df_country_review.rename(columns={'index':'country','country':'total_reviews'}, inplace=True)


# In[24]:


import matplotlib.pyplot as plt

# Assuming 'country' is the column containing country names and 'reviews' contains the review counts
df_country_review = df.groupby('country')['reviews'].count().reset_index()

# Sort the DataFrame by review count in descending order and select the top 5 countries
top_5_countries = df_country_review.sort_values(by='reviews', ascending=False).head(5)

# Create a custom_colors list with 'red' for the top country and 'gray' for others
custom_colors = ['red' if country == top_5_countries.iloc[0]['country'] else 'gray' for country in top_5_countries['country']]

# Create the bar chart with custom colors
ax = top_5_countries.plot(kind="bar", x='country', y='reviews', color=custom_colors, legend=False)

# Add labels and title
plt.title("Top 5 Countries with the Most Reviews")
plt.xlabel("Country")
plt.ylabel("Number of Reviews")

# Show the plot
plt.show()


# In[28]:


# Remove non-numeric characters from the 'stars' column and convert it to a numeric data type
df['stars'] = pd.to_numeric(df['stars'], errors='coerce')

# Now calculate the mean
df_country_rating = pd.DataFrame(df.groupby('country')['stars'].mean().sort_values(ascending=False)).reset_index()


# In[29]:


df_country_rating.rename(columns={'stars':'avg_rating'}, inplace=True)


# In[30]:


fig, ax = plt.subplots(figsize=(18,5))
ax1 = sns.barplot(x='country', y='avg_rating', data=df_country_rating[:12])
ax.bar_label(ax.containers[0])
ax.set_title("Top 12 Countries with avg highest rating provided to British Airways")


# In[31]:


#convert the date datatype to datetime

df.date = pd.to_datetime(df.date)


# In[32]:


fig = px.line(df, x='date', y="stars")
fig.update_xaxes(rangeslider_visible=True)
fig.show()


# In[33]:


import nltk
from nltk.corpus import stopwords
# Start with one review:
reviews = " ".join(df.corpus)
plt.figure(figsize=(20,10))

stopwords = set(stopwords.words('english'))

# Create and generate a word cloud image:
wordcloud = WordCloud(height=600,width=600,max_font_size=100, max_words=500, stopwords=stopwords).generate(reviews)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[34]:


import nltk
from nltk.corpus import stopwords
reviews = " ".join(df.corpus)
plt.figure(figsize=(20,10))

stopwords = set(stopwords.words('english'))
stopwords.update(["ba","flight", "british","airway", "airline","plane", "told","also","passenger"                  "london", "heathrow", "aircraft", "could","even", "would"])
# Create and generate a word cloud image:
wordcloud = WordCloud(height=500,width=500,max_font_size=100, max_words=300, stopwords=stopwords).generate(reviews)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[37]:


get_ipython().system('pip install scikit-learn')


# In[38]:


from nltk import ngrams
from nltk.probability import FreqDist

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer

#split the text of all reviews into a list of words
words = reviews.split(" ")

#remove certain words that will not be used to determine the positive or negative sentiment
stopwords = text.ENGLISH_STOP_WORDS.union(['flight', 'ba', "passenger","u", "london","airway","british","airline",                                           "heathrow","plane","lhr","review"])


new_words = [word for word in words if word not in stopwords]

nlp_words=FreqDist(new_words).most_common(20)

#create a dataframe of these word and its frequencies
all_fdist = pd.Series(dict(nlp_words))


# In[39]:


## Setting figure, ax into variables
fig, ax = plt.subplots(figsize=(15,8))

## Seaborn plotting using Pandas attributes + xtick rotation for ease of viewing
all_plot = sns.barplot(x=all_fdist.index, y=all_fdist.values, ax=ax)
all_plot.bar_label(all_plot.containers[0])
plt.xticks(rotation=30)


# In[44]:


# Unique countries BA recieved the reviews from

print(f"{len(df.country.unique())} unique countries")


# In[45]:


# Unique countries BA recieved the reviews from

print(f"{len(df.reviews.unique())} total reviews")


# In[ ]:




