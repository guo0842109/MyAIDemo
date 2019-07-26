import numpy as np
import pandas as pd

import matplotlib.pyplot as plot

# 读数据
housing = pd.read_csv('./data/kc_train.csv')
target = pd.read_csv('./data/kc_train2.csv')#销售价格
t = pd.read_csv('./data/kc_test.csv')#测试数据


# 数据预处理

housing.info()   #查看是否有缺失值

# 特征缩放
from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler()
min_max_scaler.fit(housing)#进行内部拟合