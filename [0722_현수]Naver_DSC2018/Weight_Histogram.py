# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:27:30 2018

@author: qgqg2
"""

"""
Created on Sat Jul 21 00:26:44 2018

@author: gjrm2
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import collections

# utf-8 encoding error, so I take 'cp1252'
df = pd.read_csv('laptops.csv', encoding= "cp1252")
df.shape

plt.hist(df['Price_euros'], rwidth = 0.9)
plt.xlabel('Price_euros')
plt.ylabel('#')
plt.title('Histogram of euros')
plt.show()

temp = df.pivot_table('Price_euros', index = 'Company', aggfunc = 'mean')
print(temp)

corr = df.corr()
print(corr)


#csv파일 읽어오기