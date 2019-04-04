# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:40:33 2018

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

TypeName_type = df['TypeName'].unique()
TypeName_size = df.groupby('TypeName').size()
print(TypeName_size)

labels = TypeName_type
ratio = TypeName_size


plt.figure(figsize=(13,13))
plt.pie(ratio, labels=labels, shadow=True, startangle=150, autopct = '%1.1f%%')
plt.title('TypeName of Product')
#plt.show()

