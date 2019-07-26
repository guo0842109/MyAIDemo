import numpy as np
# https://blog.csdn.net/Dorisi_H_n_q/article/details/82259786
# 1、创建一个长度为10的一维全为0的ndarray对象，然后让第5个元素等于1

# s1=np.zeros(shape=10)
# s1[4] = 1
# print(s1.shape)

# 2、创建一个元素为从10到49的ndarray对象
s2 = np.random.randint(10,50,size=10)
print(s2)

# s2 = np.linspace(10,50,10)
# print(s2)

# s2 = np.arange(10,50,5)
# print(s2)