import nltk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import model_selection
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import state_union
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

'''
NE Type and Examples:

ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian
'''

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = sent_tokenizer.tokenize(sample_text)


def processContent():
    try:
        for i in tokenized:
            words = word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # print(tagged)

            # namedEnt = nltk.ne_chunk(tagged)
            namedEnt = nltk.ne_chunk(tagged , binary=True) ## When type of the named entity is not important(puts all named entities together.
            # namedEnt.draw()
            print(namedEnt)

    except Exception as e:
        print(str(e))


processContent()
