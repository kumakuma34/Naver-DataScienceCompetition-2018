# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:44:30 2018

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

Inches_type = df['Inches'].unique()
Inches_size = df.groupby('Inches').size()
print(Inches_size)

labels = Inches_type
ratio = Inches_size


plt.figure()
plt.bar(Inches_type, Inches_size)
plt.xlabel('Inches')
plt.ylabel('#')
plt.title('# of inches')
plt.show()
