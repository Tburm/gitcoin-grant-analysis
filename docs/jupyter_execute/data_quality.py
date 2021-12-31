#!/usr/bin/env python
# coding: utf-8

# # Data Quality Checks
# 
# Key Findings:
# - Currency fields are all stored as strings (`$XXX.XX`) and need a conversion to float values
#   - `match_amount`
#   - `crowdfund_amount_contributions_usd`
#   - `total`
# - There are null values in the `total` and `crowdfund_amount_contributions_usd` fields that should be labeled `0`
# - The `region` column is not complete, with **44% of records** (2600/5900) having a value of `none` or `undefined`
#   - There is not a meaningful difference between these labels, so I am combining them and coding nulls as `none`
#   - Since there are so many missing values, this likely won't be useful for analysis
# 

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


# parse currency fields into float columns
df['match_amount'] = pd.to_numeric(df['match_amount'].str.replace('[^.0-9]', ''))
df['crowdfund_amount_contributions_usd'] = pd.to_numeric(df['crowdfund_amount_contributions_usd'].str.replace('[^.0-9]', '')).fillna(0)
df['total'] = pd.to_numeric(df['total'].str.replace('[^.0-9]', '')).fillna(0)


# In[7]:


# recode the region
df['region'] = df['region'].replace('undefined', 'none').fillna('none')


# In[8]:


df.describe()


# In[9]:


# profile the data
profile = ProfileReport(df, title="Grants Data Profile")
profile


# In[10]:


# write out the clean data
df.to_csv('../data/grants_data.csv', index=False)

