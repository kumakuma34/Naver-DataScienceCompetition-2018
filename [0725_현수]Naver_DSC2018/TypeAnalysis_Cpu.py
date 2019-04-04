# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:06:02 2018

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
Cpu_type = df['Cpu_Type'].unique()
Cpu_size = df.groupby('Cpu_Type').size()
print(Cpu_size)
print(Cpu_type)


labels = Cpu_type
ratio = Cpu_size


plt.figure(figsize=(13,13))
plt.pie(ratio, labels=labels, shadow=True, startangle=150, autopct = '%1.1f%%')
plt.title('PieChart of Cpu')
#plt.show()
