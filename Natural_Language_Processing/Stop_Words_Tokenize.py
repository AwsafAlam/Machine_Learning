# import nltk
# nltk.download()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import model_selection

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Need to find a larger library of stop_word for bigger projects

stop_words = set(stopwords.words("english"))
print(stop_words)

data = "All work and no play makes jack a dull boy, all work and no play"
print(word_tokenize(data)) #separates words


data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
print(sent_tokenize(data)) # Sentence alada kore
