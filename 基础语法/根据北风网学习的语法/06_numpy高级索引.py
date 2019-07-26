import tensorflow as tf
import numpy as np

# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
# print ('我们的数组是：' )
# print (x)
# print ('\n')
# rows = np.array([[0,0],[3,3]])
# cols = np.array([[0,2],[0,2]])
# print(rows)
# print(cols)
# y = x[rows,cols]
# print  ('这个数组的四个角元素是：')
# print (y)

# x = np.array([1,2,3]*5)
#
# print(x.reshape(3,5))
# print(x[x>2])

x = np.arange(32).reshape(8,4)
# x = np.arange(32)
print(x)
# print (x[[4,2,1,7]])
# print (x[[4,2,1,7]])
print (x[np.ix_([1,5,7,2],[0,3,1,2])])
