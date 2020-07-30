from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

iris = load_iris()
model = DecisionTreeClassifier()
model.fit(iris.data, iris.target)

print(iris.target_names)

fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot()
plot_tree(model, feature_names=iris.feature_names, ax=ax, class_names=iris.target_names, filled=True); 
plt.show()