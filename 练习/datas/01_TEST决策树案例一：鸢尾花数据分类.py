# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split#测试集和训练集
from sklearn.preprocessing import MinMaxScaler#数据归一化
from sklearn.decomposition import PCA #主成分分析

from sklearn.feature_selection import SelectKBest  #特征选择
from sklearn.feature_selection import chi2  #卡方统计

from sklearn.tree import DecisionTreeRegressor#决策树回归树
from sklearn.tree import DecisionTreeClassifier#决策树分类树
# 指定path
path = '../datas/iris.data'
data = pd.read_csv(path,header=None)
# print(data)

#获取X变量前4列
x = data[list(range(4))]
# print(x)
# print(data[4])
# 取出第四列转成0，1，2的形式
y=pd.Categorical(data[4]).codes#把Y转换成分类型的0,1,2
# print(y)

# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
#  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#  2 2]

# train_test_split函数用于将矩阵随机划分为训练子集和测试子集，并返回划分好的训练集测试集样本和训练集测试集标签。
# 格式：
# X_train, X_test, y_train, y_test = cross_validation.train_test_split(train_data, train_target, test_size=0.3,random_state=0)
# 参数解释：
# train_data：被划分的样本特征集
# train_target：被划分的样本标签
# test_size：如果是浮点数，在0-1之间，表示样本占比；如果是整数的话就是样本的数量
# random_state：是随机数的种子。
# 随机数种子：其实就是该组随机数的编号，在需要重复试验的时候，保证得到一组一样的随机数。比如你每次都填1，其他参数一样的情况下你得到的随机数组是一样的。但填0或不填，每次都会不一样。
# 随机数的产生取决于种子，随机数和种子之间的关系遵从以下两个规则：种子不同，产生不同的随机数；种子相同，即使实例不同也产生相同的随机数。

#数据进行分割（训练数据和测试数据）
x_train, x_test, y_train, y_test  = train_test_split(x,y,test_size=0.8,random_state=14)

# print(x_train)

# print(x_test)
# print(y_train)

print('训练样本 %d,测试样本 %d'%(x_train.shape[0],x_test.shape[0]))

# 因为需要体现以下是分类模型，因为DecisionTreeClassifier是分类算法，要求y必须是int类型
y_train = y_train.astype(np.int)
y_test = y_test.astype(np.int)
# print(y_train)
# print(y_test)

# 数据标准化
# 标准化是依照特征矩阵的列处理数据，其通过求z-score的方法，将样本的特征值转换到同一量纲下，常用与基于正态分布的算法，比如回归
# StandardScaler (基于特征矩阵的列，将属性值转换至服从正态分布)

# 归一化
# 提升模型收敛速度，提升模型精度，常见用于神经网络
# MinMaxScaler （区间缩放，基于最大最小值，将数据转换到0,1区间上的）

# 正则化
# 其目的在于样本向量在点乘运算或其他核函数计算相似性时，拥有统一的标准，常见用于文本分类和聚类、logistic回归中也会使用，有效防止过拟合
# Normalizer （基于矩阵的行，将样本向量转换为单位向量）


#用标准化方法对数据进行处理并转换
## scikit learn中模型API说明：
### fit: 模型训练；基于给定的训练集(X,Y)训练出一个模型；该API是没有返回值；eg: ss.fit(X_train, Y_train)执行后ss这个模型对象就训练好了
### transform：数据转换；使用训练好的模型对给定的数据集(X)进行转换操作；一般如果训练集进行转换操作，那么测试集也需要转换操作；这个API只在特征工程过程中出现
### predict: 数据转换/数据预测；功能和transform一样，都是对给定的数据集X进行转换操作，只是transform中返回的是一个新的X, 而predict返回的是预测值Y；这个API只在算法模型中出现
### fit_transform: fit+transform两个API的合并，表示先根据给定的数据训练模型(fit)，然后使用训练好的模型对给定的数据进行转换操作


# 对以上数据做归一化
ss = MinMaxScaler()
# 先训练x_train 再转换x_train
x_train = ss.fit_transform(x_train)
# 转换x_test
x_test = ss.transform(x_test)

print ("原始数据各个特征属性的调整最小值:",ss.min_)
# [0.3125     0.52631579 0.17857143 0.41666667]
print ("原始数据各个特征属性的缩放数据值:",ss.scale_)
#  [0.3125     0.52631579 0.17857143 0.41666667]

# 特征选择，从已有的特征中选择出影响目标值最大的特征属性
# 常用方法：{ 分类：F统计量、卡方系数，互信息mutual_info_classif
#         { 连续：皮尔逊相关系数 F统计量 互信息mutual_info_classif
# SelectKBest（卡方系数）

# k默认为10
ch2 = SelectKBest(chi2,k=3)

#如果指定了，那么就会返回你所想要的特征的个数

x_train = ch2.fit_transform(x_train,y_train)#训练并转换
x_test = ch2.transform(x_test)#转换

# 对类别判断影响最大的三个特征属性分布是:
select_name_index = ch2.get_support(indices=True)
print ("对类别判断影响最大的三个特征属性分布是:",ch2.get_support(indices=False))
# [ True False  True  True]
print(select_name_index)
# [0 2 3]

# 降维
# 对于数据而言，如果特征属性比较多，在构建过程中，会比较复杂，这个时候考虑将多维（高维）映射到低维的数据
# 常用方法PCA：主成分分析（无监督）；LDA：线性判别分析（有监督）类内方差最小，人脸识别，通常先做一次pca

pca=PCA(n_components=2)
#这里是为了后面画图方便，所以将数据维度设置了2维，一般用默认不设置参数就可以
x_train = pca.fit_transform(x_train)#训练并转换
x_test = pca.transform(x_test)#转换
# print("====x_train====")
# print(x_train)
# print("====x_test====")
# print(x_test)

# 模型构建
model = DecisionTreeClassifier(criterion='entropy',random_state=0)#使用信息熵，也可以选择jini
#训练模型
model.fit(x_train,y_train)
#预测模型
y_test_hat= model.predict(x_test)

# 模型评估
# print(y_test)
# reshape(-1)部分行列,改成一串
y_test2 = y_test.reshape(-1)
# print(y_test2)
result = (y_test==y_test2)
# print(result)
# [ True  True  True  True  True  True  True  True  True  True  True  True
#   True  True  True  True  True  True  True  True  True  True  True  True
#   True  True  True  True  True  True  True  True  True  True  True  True
#   True  True  True  True  True  True  True  True  True  True  True  True
#   True  True  True  True  True  True  True  True  True  True  True  True
#   True  True  True  True  True  True  True  True  True  True  True  True
#   True  True  True  True  True  True  True  True  True  True  True  True
#   True  True  True  True  True  True  True  True  True  True  True  True
#   True  True  True  True  True  True  True  True  True  True  True  True
#   True  True  True  True  True  True  True  True  True  True  True  True]
# 求均值
print ("准确率:%.2f%%" % (np.mean(result) * 100))
# 也可以通过参数获取准确率
print("准确率",model.score(x_test,y_test))#准确率或者是检测模型的有效性
# 获取标签的类型
print("标签的类型",model.classes_)
# 获取各个特征值的重要性
print("各个特征值的重要性",model.feature_importances_)



# 画图
print("=================画图=====================")

# print(x_train)
# print(x_train.T)
# print(x_train.T[0].min())
# print(x_test)
# print(x_test.T)
# print(x_test.T[0].min())

x1_min = np.min((x_train.T[0].min(), x_test.T[0].min()))#转置后取出每列的最小值
x1_min_ = np.min((x_train[0].min(), x_test[0].min()))
print(x1_min)
print(x1_min_)




























