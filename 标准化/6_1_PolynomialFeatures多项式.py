import numpy as np
from sklearn.preprocessing import PolynomialFeatures
X = np.arange(6).reshape(3, 2)
X
# array([[0, 1],
#        [2, 3],
#        [4, 5]])
poly = PolynomialFeatures(2)
poly.fit_transform(X)
# array([[  1.,   0.,   1.,   0.,   0.,   1.],
#        [  1.,   2.,   3.,   4.,   6.,   9.],
#        [  1.,   4.,   5.,  16.,  20.,  25.]])