#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df1=pd.read_csv("C:\\Users\\Ramatu\\.jupyter\\dataset\\FOA.csv" , encoding='latin-1')
df1.head()


# In[2]:


y=df1.groupby('Item')['Y2014'].sum()
y


# In[3]:


z=df1.groupby('Item')['Y2017'].sum()
z


# In[4]:


df1.describe()


# In[5]:


df1.Y2016.isnull().sum()


# In[8]:


d=df1.groupby('Element')['Y2014'].sum()
d.sum()


# In[7]:


d1=df1.groupby('Element')['Y2015'].sum()
d1.sum()


# In[9]:


d2=df1.groupby('Element')['Y2016'].sum()
d2.sum()


# In[11]:


d3=df1.groupby('Element')['Y2017'].sum()
d3.sum()


# In[12]:


d4=df1.groupby('Element')['Y2018'].sum()
d4.sum()


# In[13]:


df1.groupby('Element')['Y2018'].sum()


# In[14]:


y2=df1.Area.unique()
len(y2)


# In[18]:


dx=df1.groupby('Element')['Y2014'].sum()
dx


# In[ ]:




