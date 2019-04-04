# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:29:50 2018

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

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import collections
from sklearn import datasets, linear_model
# utf-8 encoding error, so I take 'cp1252'
df = pd.read_csv('Processed_Data.csv', encoding= "cp1252")
#df.shape()
Ram_type = df['Ram'].unique()
Ram_size = df.groupby('Ram').size()
print(Ram_size)
print(Ram_type)


labels = Ram_type
ratio = Ram_size


plt.figure(figsize=(13,13))
plt.pie(ratio, labels=labels, shadow=True, startangle=150, autopct = '%1.1f%%')
plt.title('PieChart of Ram')
#plt.show()