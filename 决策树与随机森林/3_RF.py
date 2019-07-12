from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
x = iris.data
y = iris.target


clf = RandomForestClassifier(criterion='gini',max_depth=5, n_estimators=5)

clf.fit(x,y)

print(clf.min_weight_fraction_leaf)
print(clf.max_features)
print(clf.max_depth)
print(clf.max_depth)
print(clf.criterion)
print(clf.feature_importances_)
print(clf.predict([[1,2,3,4]]))
