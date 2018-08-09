# import nltk
# nltk.download()
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import model_selection

# Importing the dataset
dataset = pd.read_csv('Code_Review.csv')
X = dataset.iloc[:, 1].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

filtered = []
Matrix = [[]]
# data = "All work and no play makes jack a dull boy, all work and no play"
# print(word_tokenize(data)) separates words
count = 0;
for sentence in X_train:
    words = word_tokenize(sentence)
    for w in words:
        if w not in stop_words:
            filtered.append(w)
    print(filtered)
    Matrix[count].append(filtered)
    count = count+1
    filtered.clear()

# print(Matrix)
# data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
# print(sent_tokenize(data)) # Sentence alada kore

# Splitting the dataset into the Training set and Test set
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
#
# from sklearn.linear_model import LinearRegression
# regressor = LinearRegression()
# regressor.fit(X_train, y_train)
#
# # Predicting the Test set results
# y_pred = regressor.predict(X_test)
#
# cv_results = model_selection.cross_val_score(regressor, X_train, y_train, cv=4, scoring='accuracy')
#
# print (cv_results.mean())
