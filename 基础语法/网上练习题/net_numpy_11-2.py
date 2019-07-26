# 11、给定一个4维矩阵，如何得到最后两维的和？
import numpy as np
# https://blog.csdn.net/Dorisi_H_n_q/article/details/82259786

s11 = np.random.random((4,4))
print(s11)
print(s11(-1,-2))
print(s11.sum(axis=(-1,-2)))