import sympy as sym

# # 定义x为变量
# x = sym.symbols('x')
# y = x**2+2*x+3
# print(y)
# # y对x求导
# print(y.diff(x))

# 求积分
# x = sym.symbols('x')
# # a = sym.Integral(sym.cos(x)*sym.exp(x), x)
# a = 2*x +2
# print(a)
# print(sym.Eq(a, a.doit()))
#
# import matplotlib as  mpl
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(-2,2,1000)
# # y = x**2+4
# # y = np.sin(x)
# y = np.cos(x)
# plt.plot(x,y,color = '#bbbbbb',lw=2,alpha = 1)
# plt.show()

# # 求导
# x = sym.symbols('x')
# y = sym.exp(x)*(sym.cos(x))/2 + sym.exp(x)*(sym.sin(x))/2
# print(y.diff(x))
# # 求积分
# z = sym.exp(x)*sym.cos(x)
# print(z.integrate(x))
# # 求导
# print(z.doit())
# # 判断相等
# print(sym.Eq(z, z.doit()))

# x,y = sym.symbols('x y')
# z =x**2+2*x+y**2+4*y+4
# dzx = z.diff(x)
# dzy = z.diff(y)
# sym.plotting.plot3d(z,(x,-10,10),(y,-10,10))
# sym.plotting.plot3d(sym.sqrt(dzx**2 +  dzy**2), (x, -10, 10), (y, -10, 10))