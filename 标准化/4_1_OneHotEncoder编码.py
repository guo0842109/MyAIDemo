import numpy as np
from sklearn import preprocessing

x_train = np.array([[0,0,3],[1,1,0],[0,2,1],[1,0,2]])

enc = preprocessing.OneHotEncoder

enc.fit(x_train)

print(enc.transform([[0,1,3]]))