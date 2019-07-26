# 10、如何根据第3列来对一个5*5矩阵排序？
import numpy as np
# https://blog.csdn.net/Dorisi_H_n_q/article/details/82259786

s11 = np.random.random((5,5))


print(s11[np.argsort(s11[:,2])])
# a = s11[[1,-1]:2]
# print(a)