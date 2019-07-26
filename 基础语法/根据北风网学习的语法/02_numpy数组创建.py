import numpy as np

'''
数组元素为随机值
'''
# a = np.empty((4,4),dtype=np.int)
# print(a)

# b = np.ones((2,3,4,5))
# print(b)

'''
asarray、array 都可以将元组或者list转换为ndarray
'''

# a = [1,2,3]
# print(type(a))
# b = np.asarray(a)
# c = np.array(a)
# print(type(b))
# print(type(c))

# d = (1,2,3)
# print(d)
# print(type(d))
# e = np.array(d)
# print(e)
# print(type(e))

'''
arange,返回ndarray对象
numpy.arange(start,stop,step,dtype)
'''
# f = np.arange(3)
# print(f)
# print(type(f))

'''
 numpy.linspace  与arange函数类似 等差数列
 numpy.logspace  等比数列
 numpy.logscale(start, stop, num, endpoint, base, dtype)
'''
# g =  np.logspace(1,2,5,True,base=2)
# print(g)
# print(type(g))

'''
    其他创建方式
    random模块
    rand  返回 0 - 1 随机值
    randn 返回一个样本具有标准正态分布
    randint 返回随机的整数，位于半开区间[low,hight)size = 10  (3,3)
    random_integers(low[, high, size])  返回随机的整数，位于闭区间
    random 返回随机浮点数
'''

h = np.random.rand(12).reshape(3,-1)
print('h=======',h)
print('h=======',type(h))

h1 = np.random.randn(12).reshape(3,-1)
print('h1=======',h1)
print('h1=======',type(h1))

h2 = np.random.randint(1,9,size=9).reshape(-1,3)
print('h2=======',h2)
print('h2=======',type(h2))









