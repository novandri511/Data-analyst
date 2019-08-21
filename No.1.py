#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt


# In[23]:


inflasi = pd.read_csv("E:\data science\Inflasi.csv")
df = pd.DataFrame(inflasi)
df['Year'] = df['Month'].str.extract('(\d{4})', expand=True)
df


# In[24]:


df.info()


# In[30]:


df["Inflasi baru"] = df["Inflasi"].str.rstrip('%').astype('float') / 100.0
df["Inflasi baru"].describe()


# In[34]:


penjelasantiaptahun = df.groupby("Year").describe()
penjelasantiaptahun


# In[36]:


df1 =pd.DataFrame(inflasi, columns=['Year', 'Inflasi baru'])
indeks=np.array(df1['Year'])
plt.barh(indeks[0:199],df1['Inflasi baru'].iloc[0:199],color="r")
plt.title("Inflasi berdasarkan Tahun")
plt.xlabel('Inflasi baru')
plt.ylabel('Year')
plt.show()


# In[ ]:





# In[ ]:




