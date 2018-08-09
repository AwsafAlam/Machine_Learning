import nltk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import model_selection
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import state_union
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

'''
Lemmatizing :
Similar operation to stemming -> Changes a word to its synonym

More powerful than stemming
Uses parts of speech to find synonyms
'''

lemmatizer = WordNetLemmatizer();

print(lemmatizer.lemmatize("Cats"))
print(lemmatizer.lemmatize("Cacti"))

print(lemmatizer.lemmatize("Cacti" , pos="n"))