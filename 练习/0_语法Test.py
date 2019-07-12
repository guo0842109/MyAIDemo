import numpy as np

# a = np.array([[0, 5], [1, 1]])
#
# print(a)
# print(np.mean(a,axis=0))

a = np.array([[1,5,3],[4,2,6]])
print(a.min()) #无参，所有中的最小值
print(a.min(0)) # axis=0; 每列的最小值
print(a.min(1)) # axis=1；每行的最小值