import numpy as np
from sklearn.preprocessing import Imputer
#用均值插补缺失值
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit([[1, 2], [np.nan, 3], [7, 6]])
Imputer(axis=0, copy=True, missing_values='NaN', strategy='mean', verbose=0)
X = [[np.nan, 2], [6, np.nan], [7, 6]]
print(imp.transform(X))
# [[ 4.          2.        ]
#  [ 6.          3.666...]
#  [ 7.          6.        ]]

#对稀疏矩阵进行缺失值插补
import scipy.sparse as sp
X = sp.csc_matrix([[1, 2], [0, 3], [7, 6]])
imp = Imputer(missing_values=0, strategy='mean', axis=0)
imp.fit(X)
Imputer(axis=0, copy=True, missing_values=0, strategy='mean', verbose=0)
X_test = sp.csc_matrix([[0, 2], [6, 0], [7, 6]])
print(imp.transform(X_test))
# [[ 4.          2.        ]
#  [ 6.          3.666...]
#  [ 7.          6.        ]]