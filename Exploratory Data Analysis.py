#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[2]:


df = pd.read_csv('Developer_USA_Dataset_GIthubJobs_cleaned.csv')


# In[3]:


df.head()


# In[4]:


df.columns


# In[5]:


def title_simplifier(title):
    if 'developer' in title.lower():
        return 'developer'
    elif 'engineer' in title.lower():
        return 'engineer'
    elif 'specialist' in title.lower():
        return 'specialist'
        return 'na'


def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'manager' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'


# In[6]:


df['job_simp'] = df['title'].apply(title_simplifier)


# In[7]:


df.job_simp.value_counts()


# In[8]:



df['seniority'] = df['title'].apply(seniority)
df.seniority.value_counts()


# In[9]:


def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'manager' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'junior' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'


# In[10]:


df['seniority'] = df['title'].apply(seniority)
df.seniority.value_counts()


# In[11]:


def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'manager' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'junior' in title.lower() or 'jr.' in title.lower() or 'junior' in description.lower():
        return 'jr'
    else:
        return 'na'


# In[12]:


df['seniority'] = df['title'].apply(seniority)
df.seniority.value_counts()


# In[13]:


def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'manager' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'junior' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'


# In[14]:


df['seniority'] = df['title'].apply(seniority)
df.seniority.value_counts()


# In[15]:


df.job_state.value_counts()


# In[16]:


df['company'] = df.company.apply(lambda x: x.replace('\n', ''))


# In[17]:


df['company']


# In[18]:


df.describe()


# In[19]:


df.columns


# In[20]:



#  Job description length 
df['desc_len'] = df['description'].apply(lambda x: len(x))
df['desc_len']


# In[21]:


df.desc_len.hist()


# In[22]:


df.columns


# In[23]:


df_cat = df[['location', 'company',  'job_state','same_state', 'python_yn', 'API_yn',
       'aws_yn', 'excel_yn', 'SQL_yn', 'job_simp', 'seniority', 'desc_len']]


# In[24]:


df.columns


# In[25]:


df_cat = df[['location', 'company',  'job_state', 'python_yn', 'API_yn',
       'aws_yn', 'excel_yn', 'SQL_yn', 'job_simp', 'seniority', 'desc_len']]


# In[26]:



for i in df_cat.columns:
    cat_num = df_cat[i].value_counts()
    print("graph for %s: total = %d" % (i, len(cat_num)))
    chart = sns.barplot(x=cat_num.index, y=cat_num)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.show()


# In[27]:


for i in df_cat[['location']].columns:
    cat_num = df_cat[i].value_counts()[:20]
    print("graph for %s: total = %d" % (i, len(cat_num)))
    chart = sns.barplot(x=cat_num.index, y=cat_num)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.show()


# In[28]:


pd.pivot_table(df, index = ['job_simp','seniority'])


# In[29]:


pd.pivot_table(df, index = ['job_state','job_simp']).sort_values('job_state', ascending = False)


# In[ ]:




