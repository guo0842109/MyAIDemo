# 6、创建一个每一行都是从0到4的5*5矩阵
import numpy as np
# https://blog.csdn.net/Dorisi_H_n_q/article/details/82259786

l = [0,1,2,3,4]
s6 = np.array(l*5)
print(s6)
print(s6.reshape(5,5))