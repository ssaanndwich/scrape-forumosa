#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response = requests.get("https://tw.forumosa.com/top")
doc = BeautifulSoup(response.text, 'html.parser')


# In[77]:


posts = doc.select('.topic-list-item')


# In[84]:


rows = []

for post in posts:
    row = {}
    row['title'] = post.select_one('a').text
    row['category'] = post.select_one('.category-name').text
    row['url'] = post.select_one('a')['href']
    row['num_views'] = post.select_one('.views').text.strip()
    row['last_reply_date'] = post.select('td')[-1].text.strip()
    rows.append(row)


# In[85]:


df = pd.DataFrame(rows)
df


# In[86]:


df.to_csv("forumosa-top-posts.csv")


# In[ ]:




