# -*- coding: utf-8 -*-
'''
shape 与 reshape
'''

import numpy as np

# a= np.random.randn(2,3);
#
# c = np.random.rand(3,3)
#
# print(c.shape)

# b= np.array(a)

# print(b.shape())

# print(np.array(a).shape(0))

a = np.array([1,2,3,4,5,6,7,8])
print(a)
a = a.reshape(-1,1)
print(a)
# reshape新生成数组和原数组公用一个内存，不管改变哪个都会互相影响。
