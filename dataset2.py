import pandas


# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
#more dataset link: https://archive.ics.uci.edu/ml/datasets.html

# Data = "https://archive.ics.uci.edu/ml/machine-learning-databases/cmc/cmc.data" #Contraceptive choice

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

print(dataset.values)

array = dataset.values

# X = array[:,0:2]
# Y = array[:,2]
#
# X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=.2, random_state=7)
#
# predictor = LogisticRegression()
#predictor = KNeighborsClassifier()
#predictor = DecisionTreeClassifier()
#predictor = GaussianNB()
#predictor = SVC()
#
# predictor.fit(X,Y)
#
# sample = [[5.1,40]] ##sample  for test
#sample = [[3.2,75]]
#
# outcome = predictor.predict(sample)
#
#cv_results = model_selection.cross_val_score(predictor, X_train, Y_train, cv=4, scoring='accuracy')

#print cv_results.mean()

print ("predicted result:")
# print (outcome)
