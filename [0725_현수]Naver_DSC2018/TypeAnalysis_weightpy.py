# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:35:04 2018

@author: qgqg2
"""

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

Weight_type = df['weight_modified']
Weight_size = df.groupby('weight_modified').size()
print(Weight_size)
print(Weight_type)

xs = [x+0.1 for x in range(5)]
labels = Weight_type
ratio = Weight_size

plt.scatter(df['weight_modified'], df['Price_euros'], color = 'b', alpha = 0.1)
plt.xlabel('Weight(kg)')
plt.ylabel('Price_eruos')
plt.title('Scatter of weight and price')