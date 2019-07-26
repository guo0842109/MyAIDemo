# 计算训练集的平均值和标准差，以便测试数据集使用相同的变换
from sklearn import preprocessing
import numpy as np

x= np.array([[1,-1,2],[2,0,0],[0,1,-1]])

scaler = preprocessing.StandardScaler().fit(x)

# 均值
print(scaler.mean_)

print(scaler.transform(x))

print(scaler.transform([[-1,1,0]]))

# 注：1）若设置with_mean=False 或者 with_std=False，则不做centering 或者scaling处理。
#
#  　　2）scale和StandardScaler可以用于回归模型中的目标值处理。