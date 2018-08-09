# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# -- Problem statement:
# We need to find our whether there is a relationship between expenses and marketing,
#  and what will yeild the max profit

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values # Different Spendings
y = dataset.iloc[:, 4].values # Profit (Dependent)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray() #Converting State from string to newmeric val

## Dummy variables created to replace categorical data

'''
Assumptions of Linear Regression :
1. Linearity 
2. Homoscedasticity
3. Multivariate normality
4. Independence of errors
5. Lack of multicollinearity

-- Before creating any linear regression model, 
we need to make sure that these conditions are satisfied
'''

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# We can never include all dummy varialbes (thus we delete the first)
# We must always omit one dummy variable from the dataset. this is a result of multicolinearity



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)