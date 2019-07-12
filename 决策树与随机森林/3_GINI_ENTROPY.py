# -*- coding:utf-8 -*-

import numpy as np
import math
# 基尼系数
# 熵
x = []
jiniS = []
enptroyS = []

for i in range(1,10,1):
    print(i)
    t = float(i)/10
    x.append(float(i) / 10)
    enptroy = (-t)*math.log2(t)+(-1)*(1-t)*math.log2(1-t)
    enptroyS.append(enptroy/2.0)
    jini = 1- (t/1.0)**2 -((1-t)/1.0)**2
    jiniS.append(jini)

import matplotlib.pyplot as plt
plt.plot(x,enptroyS,'r--',x,jiniS,'y--')
plt.show()
