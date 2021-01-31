#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:07:26 2021

@author: karanwalanj
"""


import pandas as pd
df = pd.read_csv('Developer_USA_Dataset_GIthubJobs.csv')

#Company name text only - Capitalize the first letter of each word of the company name
df['company'] = df['company'].str.title() 

#Company url - make the url lower case
df['company_url'] = df['company_url'].str.lower() 

#Drop Missing values with 'nan'
df = df.dropna() 

#Drop values with unclear city and state
df = df[df['location'] != "United States"]
df = df[df['location'] != "New Jersey "]
df = df[df['location'] != "All Locations"]

#state field 
df['job_state'] = df['location'].apply(lambda x: x.split(',')[1])
df['job_state'].value_counts()

#Add correct url to paypal
df.loc[df['company'] == 'Paypal', 'company_url'] = 'https://www.paypal.com'
#Add correct url to Your Hippo
df.loc[df['company_url'] == 'http://www.yourhippo.com', 'company'] = 'YourHippo'

#python
df['python_yn'] = df['description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#API
df['API_yn'] = df['description'].apply(lambda x: 1 if 'API' in x.upper() else 0)
#aws 
df['aws_yn'] = df['description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
#excel
df['excel_yn'] = df['description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
#MySQL
df['SQL_yn'] = df['description'].apply(lambda x: 1 if 'SQL' in x.upper() else 0)


df.columns


df.to_csv(r'/Users/karanwalanj/Desktop/Spring 2021/Web Mining/Developer_USA_Dataset_GIthubJobs_cleaned.csv', index = False)


