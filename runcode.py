#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:23:51 2021

@author: karanwalanj
"""
import glassdoor_scraper as gs 
import pandas as pd 

path = "/Users/karanwalanj/Downloads/chromedriver"

df = gs.get_jobs('data scientist',10, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)