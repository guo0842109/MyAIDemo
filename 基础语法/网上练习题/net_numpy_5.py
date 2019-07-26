# 5、创建一个10*10的ndarray对象，且矩阵边界全为1，里面全为0

import numpy as np
# https://blog.csdn.net/Dorisi_H_n_q/article/details/82259786

# s5 =np.zeros([10,10],dtype=np.float32)
# s5[:,[0,9]] = 1
# s5[[0,9],:] = 1
# print(s5)

s5 = np.ones([10,10],dtype=np.float)
s5[1:-1,1:-1] = 0
print(s5)