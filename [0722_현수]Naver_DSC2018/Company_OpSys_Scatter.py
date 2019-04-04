# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 14:38:01 2018

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

# utf-8 encoding error, so I take 'cp1252'
df = pd.read_csv('laptops.csv', encoding= "cp1252")
df.shape

Op = df.groupby('OpSys').count()
plt.figure(figsize=(18,3))
plt.scatter(df['Company'],df['OpSys'],color='g',s=10)
plt.xlabel('Company')
plt.ylabel('OpSys')
plt.title('Scatterplot of Company between OpSys')
plt.show()
#csv파일 읽어오기