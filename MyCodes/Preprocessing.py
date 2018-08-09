import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values #independent
Y = dataset.iloc[:, 3].values # Dependent

# Handling Missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'NaN' , strategy = 'mean',axis=0)
imputer.fit(X[:, 1:3])
X[: , 1:3] = imputer.transform(X[:, 1:3])

# Using Categorical Data
# We encode text into numbers to use thenm in equations
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencoder_X = LabelEncoder()
X[: ,0] = labelencoder_X.fit_transform(X[: ,0]) # Assigns values (0, 1 , 2 -> Spain , Germany , France etc)
# However 0,1,2 means one country has higher priority over another, which is npot true.
oneHotEncoder =  OneHotEncoder(categorical_features = [0])
X = oneHotEncoder.fit_transform(X).toarray() # Country is replaced by 3 columns. // Made up of 0 and 1 only


labelencoder_Y = LabelEncoder()
Y = labelencoder_X.fit_transform(Y)

# Splitting into Training set and test dataset
from sklearn.model_selection import train_test_split
X_train, X_test , Y_train , Y_test = train_test_split(X,Y , test_size = 0.2 , random_state = 0)

# Feature Scaling
# - Many Machine Learning models are based on euclidean distanceself.
# - if the variables do not increase /dec at the same rate, that can be a problemself.
# e.g  Salary => 48000 - 52000 , Age => 40 - 27 ; The euclidean distance is dominated by Salary
# So, variables must be transformed to thast they are in the same range
#  -- Feature Scaling :

# Standardisation:
# X_stand = (X - Mean(x) )/ std_Deviation(X)
#
# NormalizAtion:
# X_norm = (X - Min(x) )/ Max(X) - Min(X)
# This puts our variables in the same range

# NOTE:  Feature scaling makes our algorithm faster. (e.g Decision tree)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler(); # Declaring object of StandardScaler class

X_train = sc_X.fit_transform(X_train) # Fit the StandardScaler object to the training set and then transform it
X_test = sc_X.transform(X_test) # Same object, so no need to Fit

# Dummy variables depend on the context. Sometimes we may need to scale dummy variables also, sometimes not
# NOTE: it won't break our model if we don't scale

# -- Since this is a Classification problem with a Categorical dependent variable ( 0 ,1  -> in place of letters of the original set),
# We do not need top add Featuere Scaling to the dependent variable Y


print(X_train);
