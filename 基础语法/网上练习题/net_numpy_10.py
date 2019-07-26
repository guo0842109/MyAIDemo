# 9、创建一个长度为10的随机数组并将最大值替换为0

import numpy as np
# https://blog.csdn.net/Dorisi_H_n_q/article/details/82259786

s10 = np.random.random([10])
print(s10)
print(np.argmax(s10))
loc = np.argmax(s10)
print(np.max(s10))
s10[loc] = 0;
print(s10)
