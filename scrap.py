#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[5]:


url="https://insights.blackcoffer.com/rising-it-cities-and-its-impact-on-the-economy-environment-infrastructure-and-city-life-by-the-year-2040-2/"


# In[8]:


page=requests.get(url)


# In[11]:


page.content


# In[14]:


black=BeautifulSoup(page.content,"html.parser")


# In[16]:


black


# In[28]:


black2=black.findAll('div',attrs={"class":"td-pb-span8 td-main-content"})
black2


# In[32]:


black3=black2[0].text.replace("\n","")
black3


# In[42]:


data=[[url,black3]]
data


# In[44]:


df=pd.DataFrame(data,columns=["url","black3"])
df

