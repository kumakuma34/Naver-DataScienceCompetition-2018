# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 13:45:11 2018

@author: gjrm2

테슷흐
"""
import pandas as pd

"""
DataFrame에 넣는 과정
data = pd.read_csv('Processed_Data.csv', encoding= "cp1252")

del data['Unnamed: 0']
del data['Product']
del data['ScreenResolution']
del data['Cpu']
del data['Ram']
del data['Memory']
del data['Gpu']
del data['Weight']
del data['Cpu_modified']
del data['Memory_temp']
del data['Memory_HDD']
#del data['Opsys']

"""

import matplotlib.pyplot as plt
#plt.scatter(data.Price_euros, (data.Ram_modified>=8), alpha=0.02)


from scipy.optimize import curve_fit
import scipy


# 코드가 드럽다. 슬프다. ㅠㅠ.
# 상수들 걍 리스트 하나로 빼버릴까..?
# Inches, Cpu_Clock, Ram_modified, weight_modified, Screen_modified, Memory_SSD
def fn(x, a, b, c,d,e,f,g):
    return a + b*x[0] + c*x[1] + d*x[2] + e*x[3] + f*x[4] + g*x[5]

# 걍 일단 DataFrame에 있는 모든 row 선택했음. 사용할 컬럼은 fn함수 위에 쓴 그대로.
x = [data.Inches, data.Cpu_Clock, data.Ram_modified, data.weight_modified, data.Screen_modified, data.Memory_SSD]
y = data.Price_euros
popt, pcov = curve_fit(fn, x, y)

#pcov는 covariance니까 버리고, popt가 계산한 a~g 상수값.
# 아 근데 굳이 선형모델 아니어두 됨. fn에서 리턴 수식 바꾸면 제곱식도 쓸 수 있어

k = 435 # 선택해볼 특정 row
xk = [data.Inches[k], data.Cpu_Clock[k], data.Ram_modified[k], data.weight_modified[k], data.Screen_modified[k], data.Memory_SSD[k]]
print('예측가격 :', fn(xk, popt[0],popt[1],popt[2],popt[3],popt[4],popt[5],popt[6]), '실제가 :', y[k])


# 아직 gpu 고려를 안해서 잘 안맞는것도 있음. 맞는건 되게 유사하게 나옴.