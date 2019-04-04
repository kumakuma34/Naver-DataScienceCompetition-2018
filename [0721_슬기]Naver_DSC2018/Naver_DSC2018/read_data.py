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

plt.hist(df['Inches'], rwidth = 0.9)
plt.xlabel('Inches')
plt.title('Histogram of Inches')
plt.show()

#Inches 히스토그램 그리기



# 일단 그러면 data라는 변수에 들어가있음.
# spyder에서 우측에 variable explorer에서 더블클릭하면 직접 열어볼 수 있음


# 이제 파이썬 이용해서 통계내는 방법들을 검색하고 따라해보자!