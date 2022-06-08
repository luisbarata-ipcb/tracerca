from sklearn.datasets import load_iris
from sklearn import preprocessing
data = load_iris()
 
# separate the independent and dependent variables
X_data = data.data
target = data.target
 
# standardization of dependent variables
standard = preprocessing.scale(X_data)
print(standard)








from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
 
data = load_iris()
scale= StandardScaler()
 
# separate the independent and dependent variables
X_data = data.data
target = data.target
 
# standardization of dependent variables
scaled_data = scale.fit_transform(X_data) 
print(scaled_data)