# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

N = 100
# 生成1*N的矩阵
x = np.random.rand(N)*6-3
x.sort()
y=x*x
x = x.reshape(-1,1)
# print(x)
# figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
plt.figure(facecolor='w')
# plt.plot(x,y)
# ms：点的大小；mec:点的边框颜色
plt.plot(x, y, 'ro', ms=10, mec='k', label='实际值')

# 测试数据
x_test = np.linspace(-3,3,50).reshape(-1,1)
# 创建一个决策树
dtr =  DecisionTreeRegressor()
# 决策树的颜色及其深度
depth = [2,4,6,8,10]
clr = 'rgbmk'

for d,c in zip(depth,clr):
    #设置最大深度，预剪枝
    dtr.set_params(max_depth=d)
    #训练决策树
    dtr.fit(x, y)
    #用训练出的模型验证数据的输出
    y_hat= dtr.predict(x_test)
    #画出模型的的到的曲线
    plt.plot(x_test,y_hat,'-',color=c, linewidth=2, markeredgecolor='k', label='Depth=%d' % d)

plt.legend(loc='upper center', fontsize=12)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('DT')
# plt.tight_layout(2)
plt.show()