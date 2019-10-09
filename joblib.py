from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris 
from sklearn import metrics 
from sklearn.externals import joblib 

iris = load_iris() 
  
X = iris.data 
y = iris.target 

knn = KNeighborsClassifier(n_neighbors=3)

print(knn)


knn.fit(X,y)
print(knn.predict([[3, 5, 4, 2]]))


joblib.dump(knn, 'iris_knn.pkl')

knn_load = joblib.load('iris_knn.pkl')

print(knn_load)
