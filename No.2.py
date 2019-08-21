#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


salesmobil = pd.read_csv('E:\data science\mtcars.csv')
df = pd.DataFrame(salesmobil)


# In[15]:


df.info()


# In[16]:


df['mpg_level'] = pd.cut(df['mpg'], bins=[0,20,30,100], labels=["low", "medium", "hard"])
df


# In[5]:


sns.distplot(salesmobil['mpg'])


# In[6]:


salesmobil_corr = salesmobil.corr()
salesmobil_corr[np.abs(salesmobil_corr)<.2] = 0
plt.figure(figsize=(12,12))
sns.heatmap(salesmobil_corr,vmin=-1, vmax=1,
            cmap='coolwarm', annot=True);


# In[7]:


pd.crosstab(index=df['mpg_level'], columns=df['gear'])


# In[12]:


pd.crosstab(index=df['mpg_level'], columns=df['carb'])


# In[13]:


pd.crosstab(index=df['mpg_level'], columns=df['disp'])


# In[14]:


pd.crosstab(index=df['mpg_level'], columns=df['hp'])


# In[18]:


pd.crosstab(index=df['mpg_level'], columns=df['vs'])


# In[ ]:




