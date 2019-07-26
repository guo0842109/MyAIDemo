import numpy as np
# https://blog.csdn.net/Dorisi_H_n_q/article/details/82259786

# 使用np.random.random创建一个10*10的ndarray对象，并打印出最大最小元素

s4 = np.random.random((2,10))
print(s4)
print(np.min(s4))
print(np.max(s4))
