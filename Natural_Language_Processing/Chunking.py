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
Consider we split up a sentence by Part of speech tag.

To find the meaning of a sentence :

Named entity (in the context) -> (Person place or thing) Who the sentence is talking about. usually a noun

-> for sentence with conjunction ( can be many Named entities totally unrelated)

Chunking is done by mixing part of speech with regex

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

            chunkGram = """MyChunk: {<RB.?>*<VB.?>*<NNP>+<NN>?} """  #Zero or more of any Adverbs/ Verbs describing a noun
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            # chunked.draw()  ## Draws a parse tree
            print(chunked)

            '''Grouping together bunch of similar words using parts of speech '''
    except Exception as e:
        print(str(e))


processContent()
