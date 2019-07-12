# -*- coding:utf-8 -*-

import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
import pydot
import os
print(os.getcwd())

# 定义特征选择标准为entropy，深度为7
clf = tree.DecisionTreeClassifier(criterion="entropy",max_depth=7)
# 加载鸢尾花数据
iris = load_iris()
# 训练模型
clf.fit(iris.data,iris.target)
# 输出图
tree.export_graphviz(clf, out_file='tree.dot')
(graph,) = pydot.graph_from_dot_file('tree.dot')
graph.write_png('1.png')
graph.write_png('tree.png')

