#!/usr/bin/env python
# coding: utf-8

# # Grants Data Analysis
# 
# Key Findings:
# - Some text

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import plotly.io as pio
pio.renderers.default = "notebook"


# In[2]:


# read in clean grants data
df = pd.read_csv('../data/grants_data.csv')
df['count'] = 1
df.head()


# In[3]:


# data transformation and new variables
df['dollars_per_contributor'] = df['crowdfund_amount_contributions_usd'] / df['num_unique_contributors']


# In[4]:


fig = px.histogram(
    df,
    x='round_number',
    y='round_number'
)

fig.update_layout({
    'showlegend': False,
    'title': 'Grants per Round',
    'xaxis_title': 'round',
    'yaxis_title': 'grants',
    'xaxis_dtick': 1,
    'bargap': 0.2,
})

fig.write_image("images/grants_per_round.jpeg")
fig.show()


# In[5]:


fig = px.histogram(
    df,
    x='round_number',
    y='num_contributions'
)

fig.update_layout({
    'showlegend': False,
    'title': 'Contributions per Round',
    'xaxis_title': 'round',
    'yaxis_title': 'contributions',
    'xaxis_dtick': 1,
    'bargap': 0.2,
})

fig.write_image("images/contrib_per_round.jpeg")
fig.show()


# In[6]:


fig = px.histogram(
    df,
    x='round_number',
    y=[
        'crowdfund_amount_contributions_usd',
        'match_amount'
    ]
)

fig.update_layout({
    'title': 'Contributions per Round',
    'xaxis_title': 'round',
    'yaxis_title': 'contributions ($)',
    'xaxis_dtick': 1,
    'yaxis_tickprefix': '$',
    'yaxis_tickformat': ',.0f',
    'bargap': 0.2
})

fig.write_image("images/contrib_per_round_match.jpeg")
fig.show()


# ## Questions:
# * Holy moly round 12
#   * Most recent round 12 had a huge increase in both crowdfunded contributions as well as matched contributions

# ## Round 8
# ### Questions
# * What happened during round 8?
#   * There was a significant increase in crowdfunding contributions
#   * Was this one big donation? Bigger marketing campaign?
# 
# ### Key Findings
# * Round 8 had a big increase in individual contribution compared to previous rounds
# * The grant with the most funding in round 8 (Coin Center) had more contributions than nearly every grant in round 7 combined
# * The higher total amount is driven by crowdfunding, not by a larger matched amount
# * Round 8 had the lowest proportion of contributions coming from matches, so it looks more like organic growth of contributions
#   * It is difficult to figure out from this dataset, since all contributions are aggregated
#   * This could potentially be a single large donation

# In[7]:


fig = px.histogram(
    df,
    x='round_number',
    y='num_contributions'
)

fig.update_layout({
    'showlegend': False,
    'title': 'Contributions per Round',
    'xaxis_title': 'round',
    'yaxis_title': 'contributions',
    'xaxis_dtick': 1,
    'bargap': 0.2,
})

fig.write_image("images/contributions_per_round.jpeg")
fig.show()


# In[8]:


df.loc[df.round_number == 8, :].groupby('grant_title')['total'].sum(
).sort_values(ascending=False).reset_index().head(20)


# ## Round 12
# ### Questions
# * What drove the significant increase in donations during round 12?
# 
# ### Key Findings
# * Both contributions and matches went up by similar amounts in this round
# * Significant increase to "Community" project category
# * Lots of projects in the "Grants round 12" category which seems like bad data
# * Proportion of contributions coming from a match is going up, with round 12 being a local maximum
# * NFT contributions almost doubled compared to round 11
# * Community projects saw the largest increase compared to round 11
# 

# In[9]:


df.loc[df.round_number == 12, :].groupby('grant_title')['total'].sum().sort_values(ascending=False).reset_index().head(20)


# In[10]:


df.loc[df.round_number == 12, :].groupby('grant_title')[['crowdfund_amount_contributions_usd', 'dollars_per_contributor']].sum(
).sort_values('dollars_per_contributor', ascending=False).reset_index().head(20)


# In[11]:


df_round = df.groupby('round_number')[['match_amount', 'crowdfund_amount_contributions_usd', 'total']].sum().reset_index()
df_round['match_proportion'] = df_round['match_amount'] / df_round['total']
df_round


# In[12]:


fig = px.line(
    df_round,
    x='round_number',
    y='match_proportion'
)

fig.update_layout({
    'showlegend': False,
    'title': 'Proportion of contributions from match',
    'xaxis_title': 'round',
    'yaxis_title': 'match %',
    'yaxis_tickformat': ',.0%',
    'yaxis_rangemode': 'tozero'
})

fig.write_image("images/proportion_from_match.jpeg")
fig.show()


# In[13]:


fig = px.histogram(
    df,
    x='round_number',
    y='crowdfund_amount_contributions_usd',
    color='category'
)

fig.update_layout({
    'title': 'Contributions by Category',
    'xaxis_title': 'round',
    'yaxis_title': 'contribution ($)',
    'bargap': 0.2,
    'yaxis_tickprefix': '$',
    'yaxis_tickformat': ',.0f',
    'yaxis_rangemode': 'tozero'
})

fig.write_image("images/contrib_per_category.jpeg")
fig.show()


# In[14]:


fig = px.histogram(
    df,
    x='round_number',
    y='crowdfund_amount_contributions_usd',
    color='category'
)

fig.update_layout({
    'title': 'Contributions by Category',
    'xaxis_title': 'round',
    'yaxis_title': 'contribution ($)',
    'bargap': 0.2,
    'yaxis_tickprefix': '$',
    'yaxis_tickformat': ',.0f',
    'yaxis_rangemode': 'tozero'
})

fig.write_image("images/contrib_per_category.jpeg")
fig.show()


# In[15]:


fig = px.histogram(
    df,
    x='round_number',
    y='count',
    color='category'
)

fig.update_layout({
    'title': 'Grants by Category',
    'xaxis_title': 'round',
    'yaxis_title': 'grants',
    'bargap': 0.2,
    'yaxis_tickformat': ',.0f',
    'yaxis_rangemode': 'tozero'
})

fig.write_image("images/grants_per_category.jpeg")
fig.show()


# In[ ]:




