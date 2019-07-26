import numpy as np

# arr = np.arange(5,11)
# print(arr)
# # 从索引2开始到索引7结束，间隔为2
# arr2 = arr[2:7:2]
# print(arr2)
#
# arr3 = slice(2,7,2)
# print(arr[arr3])

# brr = [
#     [[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]]
# ]
# print(type(brr))
# arr = np.array(brr)
# print(type(arr))
# print(np.array(brr))
# print(np.array(brr[1][1][1]))
# print(arr[1,1,2:])
# print(np.array(brr)[1,1,0:])

'''
    NumPy - 高级索引  花式索引
    如果一个ndarray是非元组序列，数据类型为整数或布尔值的ndarray，或者至少一个元素为序列对象的元组，
    我们就能够用它来索引ndarray。高级索引始终返回数据的副本。 与此相反，切片只提供了一个视图。
    整数索引
    这种机制有助于基于 N 维索引来获取数组中任意元素。 每个整数数组表示该维度的下标值。 
    当索引的元素个数就是目标ndarray的维度时，会变得相当直接。
'''

# a = np.arange(9).reshape(3,3)
# print(a)
# 索引找出00，11，22的值
# print(a[[0,1,2],[0,1,2]])

# 笛卡尔积的映射
# num = a[np.ix_([0,1,2],[0,1])]
# print(num)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# [[0 1]
#  [3 4]
#  [6 7]]

# num2 = a[[[0,0],[2,2]],[[0,2],[0,2]]]
# print(num2)


# arr1 = np.empty((8,4))
#
# for i in range(8):           # 每一行赋值为0~7
#     arr1[i] = i
# print(arr1)
# print(arr1[[4,3,0,6]])
# 选取第4行、第3行、第0行、第6行


# 多维数组
# arr4 = np.random.random((4,4))
# print(arr4)
# # 从第一行开始切割一直到最后
# print(arr4[1:])
# #  从第一行开始切割一直到最后，再切割第三列一直到最后
# print(arr4[1:,2:])


'''
高级索引
数组可以由整数数组索引、布尔索引及花式索引。
'''
# arr5 = np.random.random((5,5))
# arr5 = np.array([[1,  2],  [3,  4],  [5,  6]])
# print(arr5)
# # loc5 = np.array([[1,1],[0,0],[2,2]])
# loc5 = np.array([[1],[1]])
# print(arr5[loc5])




















