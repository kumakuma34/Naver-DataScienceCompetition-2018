# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 14:13:32 2018

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
#csv파일 읽어오기
plt.figure(figsize=(8,3))

plt.scatter(df['TypeName'],df['Inches'],color='g',s=10)

plt.xlabel('TypeName')
plt.ylabel('Inches')
plt.title('Scatterplot of Inches between TypeName')
plt.show()