# 绝对值最大标准化
# 它通过除以最大值将训练集缩放至[-1,1]。这意味着数据已经以０为中心或者是含有非常非常多０的稀疏数据
from sklearn import preprocessing
import numpy as np

x_train= np.array([[1,-1,2],[2,0,0],[0,1,-1]])

max_abs_scaler = preprocessing.MaxAbsScaler()

x_train_maxabs = max_abs_scaler.fit_transform(x_train)

print(x_train_maxabs)

x_test = np.array([[-3,-1,4]])
x_test_maxabs = max_abs_scaler.transform(x_test)
print(x_train_maxabs)