'''Text classifier for sentiment analysis'''
import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)) , category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# documents = []
# for category in movie_reviews.catagories():
#     for fileid in movie_reviews.fileids(category):
#         documents.append((list(movie_reviews.words(fileid)) , category))
#

random.shuffle(documents) ## used to created train and test sets
# print(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

print(all_words.most_common(15))
print(all_words["stupid"]) ## Number of times stupid appears in a review -_-

## Now, we can categorize the reviews by whether most of the words are positive or negative

word_features = list(all_words.keys())[:3000]  ## Getting top 3000 words, using the frequency distribution

def find_features(document):
    words = set(document)
    features = {}

    for w in word_features:
        features[w] = (w in words) ## Returns bool value

    return  features

# print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

featuresets = [(find_features(rev) , category)
               for (rev, category) in documents]

# print(featuresets)

'''
Naive Bayes algo to categorize whether it is positive or negative review
'''

train = featuresets[:1900]
test = featuresets[1900:]

# Algorithm : Naive Bayes ( Scalable, and requires less processing power )
# posterior = prior occurences x likelihood / evidence

classifier = nltk.NaiveBayesClassifier.train(train)


print("Naive Bayes algo accuracy :", (nltk.classify.accuracy(classifier , test))*100)
classifier.show_most_informative_features(15)


## Using nltk with sklearn
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB , GaussianNB , BernoulliNB  ##Multinomial Distribution
from sklearn.linear_model import LogisticRegression , SGDClassifier
from sklearn.svm import SVC , LinearSVC , NuSVC
## Each classifier of sklearn comes with its own parameters which can be used to improve its accuracy

MNB_classifier = SklearnClassifier(MultinomialNB)

MNB_classifier.train(train)
print("MNB_classifier algo accuracy :", (nltk.classify.accuracy(MNB_classifier , test))*100)


# GNB_classifier = SklearnClassifier(GaussianNB)
#
# GNB_classifier.train(train)
# print("GNB_classifier algo accuracy :", (nltk.classify.accuracy(GNB_classifier , test))*100)
#
# BNB_classifier = SklearnClassifier(BernoulliNB)
#
# BNB_classifier.train(train)
# print("MNB_classifier algo accuracy :", (nltk.classify.accuracy(BNB_classifier , test))*100)

## --> From multiple classifiers, we take a vote of which to use
## -> Accuracy of score, and also (Confidence / uncertainity) e.g 4/6 gives positive. so, pretty high certainity of positive.

