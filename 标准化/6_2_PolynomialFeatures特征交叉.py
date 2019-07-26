# 然而有时候我们只需要特征的交叉项，可以设置interaction_only=True来得到：
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

X = np.arange(9).reshape(3, 3)
X
# array([[0, 1, 2],
#        [3, 4, 5],
#        [6, 7, 8]])
poly = PolynomialFeatures(degree=3, interaction_only=True)
poly.fit_transform(X)
# array([[   1.,    0.,    1.,    2.,    0.,    0.,    2.,    0.],
#        [   1.,    3.,    4.,    5.,   12.,   15.,   20.,   60.],
#        [   1.,    6.,    7.,    8.,   42.,   48.,   56.,  336.]])