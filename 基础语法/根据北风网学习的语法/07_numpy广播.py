import numpy as np

a = np.array([[1,2,3,4],[4,3,2,1]])
b = np.array([10,20,30,40])
'''
 如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，
 那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。
'''
c = a * b
c1 = np.multiply(a,b)
print(c)
print(c1)

'''
    数组的矩阵积
    两个二位矩阵，满足第一个矩阵的列数与第二个矩阵的行数相同，那么就可以进行矩阵的乘法，即矩阵积
'''

c2 = np.matmul(a,b)
c3 = np.dot(a,b)
print(c2)
print(c3)

# a = np.array([[ 0, 0, 0],
#            [10,10,10],
#            [20,20,20],
#            [30,30,30]])
# b = np.array([1,2,3])
# print(a + b)