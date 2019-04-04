# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:09:31 2018

@author: qgqg2
"""


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import collections
from sklearn import datasets, linear_model
# utf-8 encoding error, so I take 'cp1252'
df = pd.read_csv('Processed_Data.csv', encoding= "cp1252")
df = df.drop('Unnamed: 0',1)

df['Cpu_type_modified'] = df['Cpu']
df.loc[df["Cpu_Type"] == 'i3', "Cpu_type_modified"] =3 
df.loc[df["Cpu_Type"] == 'i5', "Cpu_type_modified"] =5 
df.loc[df["Cpu_Type"] == 'i7', "Cpu_type_modified"] =7 
df.loc[(df["Cpu_Type"] != 'i3') & (df["Cpu_Type"] != 'i5') & (df["Cpu_Type"] != 'i7'), "Cpu_type_modified"] = '0'
df['Cpu__type_modified'] = df['Cpu_type_modified'].apply(pd.to_numeric)

df['Cpu_Company'] = df.Cpu.apply(lambda e: e.split()[0])
Price_by_Cpu = df.groupby('Cpu_Company').mean()
print(Price_by_Cpu['Price_euros'])

commonData = df.loc[df['Company'] == 'Dell']
commonData = commonData.loc[commonData['TypeName'] == 'Notebook']
commonData = commonData.loc[commonData['OpSys'] == 'Windows 10']


Corr = df.corr()