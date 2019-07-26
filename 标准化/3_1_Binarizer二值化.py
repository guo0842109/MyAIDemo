# 特征二值化
from sklearn import preprocessing
import numpy as np

x_train = np.array([[1,-1,2],[2,0,0],[0,1,-1]])

binarizer =preprocessing.Binarizer().fit(x_train)

print(binarizer)

print(binarizer.transform(x_train))

# 调整阈值
binarizer2 = preprocessing.Binarizer(threshold=1.1)
binarizer3 = preprocessing.binarize(x_train,threshold=1.1)

print(binarizer2.transform(x_train))

print(binarizer3)