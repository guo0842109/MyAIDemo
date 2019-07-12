# -*- coding: utf-8 -*-


from sklearn.datasets import load_iris
from sklearn import tree
import os
import pydot # need install
#import pydotplus


print(os.getcwd())
clf = tree.DecisionTreeClassifier(criterion = "entropy", max_depth=7)
iris = load_iris()
clf = clf.fit(iris.data, iris.target)
tree.export_graphviz(clf, out_file='tree.dot')
(graph,) = pydot.graph_from_dot_file('tree.dot')
graph.write_png('1.png')
graph.write_png('tree.png')


# not good for show overfitting here
X = iris.data
y = iris.target
from sklearn.model_selection import KFold
kf = KFold(n_splits=10)
score = 0.0
for train_index, test_index in kf.split(X):
    #print('train_index', train_index, 'test_index', test_index)
    train_X, train_y = X[train_index], y[train_index]
    test_X, test_y = X[test_index], y[test_index]
    clf = clf.fit(train_X, train_y)
    score += (clf.score(test_X, test_y))
    #break
print (score / 10.0)