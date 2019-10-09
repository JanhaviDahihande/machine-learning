from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris 
iris = load_iris() 
  
X = iris.data 
y = iris.target 

knn = KNeighborsClassifier(n_neighbors=3)

print(knn)


knn.fit(X,y)
print(knn.predict([[3, 5, 4, 2], [2, 3, 5, 4]]))

