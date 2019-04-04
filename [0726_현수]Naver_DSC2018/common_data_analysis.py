# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 19:58:15 2018

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

"""
지금 짜려고 하는거...
일단 가장 commmon한 데이터 들을 골라서 그거와 weight와 price간의 scatter그리기
그리고 전의 scatter와 비교하기?

OS 있는 것과 없는 것 비교하기..
"""

commonData = df.loc[df['Company'] == 'Dell']
commonData = commonData.loc[commonData['TypeName'] == 'Notebook']
ommonData = commonData.loc[commonData['Inches'] == 15.6]
#commonData = commonData.loc[commonData['Screen_modified'] == 19.2]
#commonData = commonData.loc[commonData['Cpu_Type'] == 'i5']
#commonData = commonData.loc[commonData['Ram'] == '8GB']
commonData = commonData.loc[commonData['OpSys'] == 'Windows 10']

#plt.scatter(commonData['Screen_modified'], commonData['weight_modified'], color = 'b', alpha = 0.5)
#plt.xlabel('ScreenResolution(modified)')
#plt.ylabel('Price_eruos')
#plt.title('Scatter of ScreenResolution and price (by CommonData)')

Corr = commonData.corr()

hasOS = df.loc[df['OpSys'] != 'No OS']
NoOS = df.loc[df['OpSys'] == 'No OS']

hasOS_Price_mean = hasOS.Price_euros.mean()
NoOS_Price_mean = NoOS.Price_euros.mean()

plt.hist(NoOS['Price_euros'], rwidth = 0.9, color = 'r')
plt.title('Histogram of price without OS')
plt.show()