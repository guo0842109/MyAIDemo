# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd

# 只要随机数种子seed相同，产生的随机数系列就相同
rng = np.random.RandomState(1)
x = np.linspace(0,6,100).reshape(-1,1)
x = np.linspace(0,6,100)[:,np.newaxis]#转置
# print(x)
# ravel()的作用是将多维数组变为1维数组
y = np.sin(x).ravel()+np.sin(6*x).ravel()
print(y)
