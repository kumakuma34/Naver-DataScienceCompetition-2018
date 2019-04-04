# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:34:45 2018

@author: qgqg2
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 21:51:31 2018

@author: qgqg2
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:51:29 2018

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
from sklearn import datasets, linear_model
# utf-8 encoding error, so I take 'cp1252'
df = pd.read_csv('Processed_Data.csv', encoding= "cp1252")
#df.shape()

Product_type = df['Product'].unique()
Product_size = df.groupby('Product').size()
print(Product_type)

labels = Product_type
ratio = Product_size


plt.figure(figsize=(15,15))
plt.pie(ratio, labels=labels, shadow=True, startangle=150, autopct = '%1.1f%%')
plt.title('piechart of Product')
#plt.show()

