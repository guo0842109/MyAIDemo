import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import matplotlib as mpl

#待拟合的函数，x是变量，p是参数
def func(x, p):
    a, b, c, d, e, f = p
    return a+b*x+c*x**2+d*x**3+e*x**4+f*x**5

#计算真实数据和拟合数据之间的误差，p是待拟合的参数，x和y分别是对应的真实数据
def error(p, x, y):
    return func(x, p) - y

#一组真实数据，在a=2, b=1的情况下得出
x1 = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y1 = np.array([3, 2, 7, 9, 6, 13], dtype=float)

#调用拟合函数，第一个参数是需要拟合的差值函数，第二个是拟合初始值，第三个是传入函数的其他参数
r = leastsq(error, [1, 1, 1, 1, 1, 1], args=(x1, y1))

#打印结果，r[0]存储的是拟合的结果，r[1]、r[2]代表其他信息
x = np.linspace(1,6,1000)
y = func(x, r[0])
plt.plot(x,y, lw=2, alpha=0.4)
plt.scatter(x1, y1)
plt.show()