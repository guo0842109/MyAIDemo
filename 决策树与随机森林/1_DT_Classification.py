# -*- coding:utf-8 -*-

import numpy as np
from sklearn import tree



# 使用简单的决策树，预测模型


# x = [[1,2,3,0],[4,5,6,0],[7,8,9,0]]
x = [[1,1,1]]
print("x=======")
print(x)
# y = [1,2,3]
y = [2]
print("y=======")
print(y)
# criterion 特征选择标准 默认是mse
# clf = tree.DecisionTreeClassifier(criterion = "entropy")
clf = tree.DecisionTreeRegressor(max_depth=3)
# clf.fit(x,np.array(y).reshape(-1,1))
clf.fit(x,y)

result = clf.predict([[4,5,6]])
print(result)
