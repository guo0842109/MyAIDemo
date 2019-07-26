# scale----零均值单位方差
from sklearn import preprocessing
import numpy as np

x= np.array([[1,-1,2],[2,0,0],[0,1,-1]])
x_scaled = preprocessing.scale(x)
print(x)
print(x_scaled)
print(x_scaled.mean())
print(x_scaled.std())

# [[ 1 -1  2]
#  [ 2  0  0]
#  [ 0  1 -1]]
#
# [[ 0.         -1.22474487  1.33630621]
#  [ 1.22474487  0.         -0.26726124]
#  [-1.22474487  1.22474487 -1.06904497]]
#
# 4.9343245538895844e-17
#
# 1.0