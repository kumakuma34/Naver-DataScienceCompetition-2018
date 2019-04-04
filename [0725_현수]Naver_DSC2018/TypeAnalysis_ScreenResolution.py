# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:59:11 2018

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
#df.shape()

Screen_type = df['Screen_modified'].unique()
Screen_size = df.groupby('Screen_modified').size()
S#ceen_size = Screen_size.rop('column_name', 1)
print(Screen_type)

labels = Screen_type
ratio = Screen_size

plt.figure()
plt.bar(Screen_type, Screen_size)
plt.xlabel('ScreenResolution_ranked')
plt.ylabel('#')
plt.title('Barchart of ScreenResolution')
plt.show()