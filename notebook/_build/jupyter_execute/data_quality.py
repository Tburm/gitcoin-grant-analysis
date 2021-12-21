#!/usr/bin/env python
# coding: utf-8

# # Grants: Data quality checks

# In[1]:


from decimal import Decimal
from re import sub
import pandas as pd
from pandas_profiling import ProfileReport


# In[2]:


# some data cleaning functions
def parseMoney(money):
    money = Decimal(sub(r'[^\d.]', '', money))
    return money


# In[3]:


df = pd.read_csv('../data/grants_data_raw.csv')


# In[4]:


# inspect it
df.head()


# In[5]:


df.dtypes


# In[6]:


# parse these into float columns
df['match_amount'] = pd.to_numeric(df['match_amount'].str.replace('[^.0-9]', ''))
df['crowdfund_amount_contributions_usd'] = pd.to_numeric(df['crowdfund_amount_contributions_usd'].str.replace('[^.0-9]', ''))
df['total'] = pd.to_numeric(df['total'].str.replace('[^.0-9]', ''))

# df['match_amount'] = df['match_amount'].apply(lambda x: parseMoney(x))
# df['crowdfund_amount_contributions_usd'] = df['crowdfund_amount_contributions_usd'].apply(lambda x: parseMoney(x))
# df['total'] = df['total'].apply(lambda x: parseMoney(x))


# In[7]:


df.describe()


# In[8]:


# profile the data
profile = ProfileReport(df, title="Grants Data Profile")
profile


# In[9]:


# write out the clean data
df.to_csv('../data/grants_data.csv', index=False)

