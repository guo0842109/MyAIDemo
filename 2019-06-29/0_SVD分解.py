import numpy as np


# M = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# print()
#
# U,A,V = np.linalg.svd(M,full_matrices=True)
# print(U)
# print(A)
# print(V)
#
#
# m = np.shape(U)[0]
# print(m)
# n = np.shape(V)[0]
# print(n)
# mn = np.min([m,n])
# print('mn',mn)
# Lambda = np.zeros([m,n])
# print(Lambda)
# # diag 对角线取值
# Lambda[:mn,:mn] = np.diag(A)
# print(Lambda)
#

# x = np.random.rand(5,3)
# S,A,V = np.linalg.svd(x)
# print(S)
# print(A)
# print(V)
# M = np.diag(A)
# print(M)
# # print(x)