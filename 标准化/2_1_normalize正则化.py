from sklearn import preprocessing
import numpy as np


x_train = np.array([[1,-1,2],[2,0,0],[0,1,-1]])
x_normalized = preprocessing.normalize(x_train,norm='l2')
print(x_normalized)


# 可以使用processing.Normalizer()类实现对训练集和测试集的拟合和转换
normalizer = preprocessing.Normalizer().fit(x_train)
print(normalizer)
print(normalizer.transform(x_train))