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

from pyecharts import Geo

data = [("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",
          width=1200, height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
geo.render("echarts/geo.html")
geo
