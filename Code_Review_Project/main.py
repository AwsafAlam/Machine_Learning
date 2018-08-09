import nltk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import model_selection
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer



# Importing the dataset
dataset = pd.read_csv('Code_Review.csv')
X = dataset.iloc[:, 1].values
Y = dataset.iloc[:, 2].values


# getting stop_words
stop_words = set(stopwords.words("english"))

ps = PorterStemmer()

Matrix = []

for sentence in X:
    filtered = []
    words = word_tokenize(sentence)
    # words = PunktSentenceTokenizer(sentence)
    for w in words:
        ps.stem(w) # Stemming all the words
        if w not in stop_words:
            filtered.append(w)
    l = np.asarray(filtered)
    tagged = nltk.pos_tag(l)
    print(tagged)

    # Matrix.append(l)
    Matrix.append(tagged)

X = np.asarray(Matrix)
# print(X)
for col in X:
    l = np.asarray(col)
    print(l)


# # Handling Missing data
# from sklearn.preprocessing import Imputer
#
# imputer = Imputer(missing_values = 'NaN' , strategy = 'mean',axis=0)
# imputer.fit(X[:, 1:3])
# X[: , 1:3] = imputer.transform(X[:, 1:3])

# # Using Categorical Data
# # We encode text into numbers to use them in equations
# from sklearn.preprocessing import LabelEncoder , OneHotEncoder
# labelencoder_X = LabelEncoder()
# X[: ,0] = labelencoder_X.fit_transform(X[: ,0]) # Assigns values (0, 1 , 2 -> Spain , Germany , France etc)
# # However 0,1,2 means one country has higher priority over another, which is not true.
# oneHotEncoder =  OneHotEncoder(categorical_features = [0])
# X = oneHotEncoder.fit_transform(X).toarray() # Country is replaced by 3 columns. // Made up of 0 and 1 only
#
# labelencoder_Y = LabelEncoder()
# Y = labelencoder_X.fit_transform(Y)
#
# Splitting into Training set and test dataset
from sklearn.model_selection import train_test_split
X_train, X_test , Y_train , Y_test = train_test_split(X,Y , test_size = 0.2 , random_state = 0)

# # Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler(); # Declaring object of StandardScaler class
#
# X_train = sc_X.fit_transform(X_train) # Fit the StandardScaler object to the training set and then transform it
# X_test = sc_X.transform(X_test) # Same object, so no need to Fit


# from sklearn.linear_model import LinearRegression
# regressor = LinearRegression()
# regressor.fit(X_train, Y_train)
#
# # Predicting the Test set results
# y_pred = regressor.predict(X_test)

# cv_results = model_selection.cross_val_score(regressor, X_train, Y_train, cv=4, scoring='accuracy')

# print (cv_results.mean())
