from sklearn import datasets


iris = datasets.load_iris()

'''
load_boston()	Load and return the boston house-prices dataset (regression).
load_iris()	Load and return the iris dataset (classification).
load_diabetes()	Load and return the diabetes dataset (regression).
load_digits()	Load and return the digits dataset (classification).
load_linnerud()	Load and return the linnerud dataset (multivariate regression).
load_wine()	Load and return the wine dataset (classification).
load_breast_cancer()	Load and return the breast cancer wisconsin dataset (classification).

'''

print iris.feature_names
print iris.data
print iris.target