# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:51:29 2018

@author: qgqg2
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 00:26:44 2018

@author: gjrm2
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import collections
from sklearn import datasets, linear_model

# utf-8 encoding error, so I take 'cp1252'
df = pd.read_csv('laptops.csv', encoding= "cp1252")
df.shape
df = df.drop('Unnamed: 0',1)
#쓸데없는 컬럼 버리기!!
df['Cpu_modified'] = df['Cpu']
df['Cpu_Type'] = df.Cpu.apply(lambda e: e.split()[2])
df['Cpu_Clock'] = df.Cpu.apply(lambda e: e.split()[-1])
df['Cpu_Clock'] = df.Cpu_Clock.apply(lambda x: x[0: -3])
df['Cpu_Clock'] = df['Cpu_Clock'].apply(pd.to_numeric)
df.loc[(df["Cpu_Type"] != 'i3') & (df["Cpu_Type"] != 'i5') & (df["Cpu_Type"] != 'i7'), "Cpu_Type"] = 'etc'
df.loc[(df["Cpu_Type"] != 'i3') & (df["Cpu_Type"] != 'i5') & (df["Cpu_Type"] != 'i7'), "Cpu_modified"] = 2.5 + df["Cpu_Clock"]/4
df.loc[df["Cpu_Type"] == 'i3', "Cpu_modified"] =3 + df["Cpu_Clock"]/4
df.loc[df["Cpu_Type"] == 'i5', "Cpu_modified"] =5 + df["Cpu_Clock"]/4
df.loc[df["Cpu_Type"] == 'i7', "Cpu_modified"] =7 + df["Cpu_Clock"]/4
df['Cpu_modified'] = df['Cpu_modified'].apply(pd.to_numeric)
#Cpu부분 modify해서 우선순위 매기기(수치화?)

df['Ram_modified'] = df.Ram.apply(lambda x: x[0:-2])
df['Ram_modified'] = df['Ram_modified'].apply(pd.to_numeric, errors = 'coerce')
#Ram부분 우선순위 매기기

df['weight_modified'] = df.Weight.apply(lambda x: x[0:-2])
df['weight_modified'] = df['weight_modified'].apply(pd.to_numeric)
#Weight 부분 우선순위 매기기
df['Screen_modified'] = df.ScreenResolution.apply(lambda e: e.split()[-1])
df['Screen_modified'] = df.Screen_modified.apply(lambda x: x[0:4])
df['Screen_modified'] = df['Screen_modified'].apply(pd.to_numeric)
df["Screen_modified"] = df["Screen_modified"]/100
#해상도 부분 우선순위 매기기

df['Memory_temp'] = df.Memory.apply(lambda e: e.split()[1])
df['Memory_SSD'] = df['Memory_temp']
df['Memory_SSD'].fillna(0)
df.loc[df['Memory_temp'] == 'SSD' ,"Memory_SSD"] = df['Memory'].apply(lambda e: e.split()[0])
df.loc[df['Memory_temp'] != 'SSD', "Memory_SSD"] = '-1GB'
df['Memory_SSD'] = df.Memory_SSD.apply(lambda x :x[0:-2])
df.loc[df['Memory_SSD'] == '1' ,"Memory_SSD"] = '1024'
df['Memory_SSD'] = df['Memory_SSD'].apply(pd.to_numeric)

df['Memory_HDD'] = df['Memory_temp']
df['Memory_HDD'].fillna(0)
df.loc[df['Memory_temp'] == 'HDD' ,"Memory_HDD"] = df['Memory'].apply(lambda e: e.split()[0])
df.loc[df['Memory_temp'] != 'HDD', "Memory_HDD"] = '-1GB'
df['Memory_HDD'] = df.Memory_HDD.apply(lambda x :x[0:-2])
df.loc[df['Memory_HDD'] == '1' ,"Memory_HDD"] = '1024'
df['Memory_SSD'] = df['Memory_SSD'].apply(pd.to_numeric)
#메모리 전처리

df.to_csv('Processed_Data.csv')
#전처리 후 저장!!!!!!!
#csv파일 읽어오기