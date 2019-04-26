import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values #independent
Y = dataset.iloc[:, 3].values # Dependent

# Splitting into Training set and test dataset
from sklearn.model_selection import train_test_split

X_train, X_test , Y_train , Y_test = train_test_split(X,Y , test_size = 0.2 , random_state = 0)

# Feature Scaling
'''
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler(); # Declaring object of StandardScaler class

X_train = sc_X.fit_transform(X_train) # Fit the StandardScaler object to the training set and then transform it
X_test = sc_X.transform(X_test) # Same object, so no need to Fit
'''

print(X_train)
