# 另外一种标准化方法是将数据缩放至给定的最小值与最大值之间，通常是０与１之间，
# 可用MinMaxScaler实现。或者将最大的绝对值缩放至单位大小，可用MaxAbsScaler实现。
# 使用这种标准化方法的原因是，有时数据集的标准差非常非常小，有时数据中有很多很多零（稀疏数据）需要保存住０元素。

# MinMaxScaler(最小最大值标准化)
# 公式：X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0)) ;
# X_scaler = X_std/ (max - min) + min

# MinMaxScaler(最小最大值标准化)
from sklearn import preprocessing
import numpy as np
# 例子，将数据缩放至[0，1]间
x_train = np.array([[1,-1,2],[2,0,0],[0,1,-1]])
min_max_scaler = preprocessing.MinMaxScaler()
x_train_minmax= min_max_scaler.fit_transform(x_train)
print(x_train_minmax)

# 将上述得到的scale参数应用到测试数据

x_test = np.array([[-3,-1,4]])
x_test_train = min_max_scaler.transform(x_test)
print(x_test_train)

#可以用以下方法查看scaler的属性
print(min_max_scaler.scale_)
print(min_max_scaler.min_)

'''
[[0.5        0.         1.        ]
 [1.         0.5        0.33333333]
 [0.         1.         0.        ]]

[[-1.5         0.          1.66666667]]

[0.5        0.5        0.33333333]

[0.         0.5        0.33333333]
'''

