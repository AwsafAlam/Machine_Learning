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
Chinking : Removal of some words from a group of words.

--> During the process of chunking , sometimes we do not want certain words to be together. 
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

            chunkGram = """MyChunk: {<.*>+} 
                                    }<VB.?|IN|DT|TO>+{"""  #Chunk everything then get rid of verb or preposition
            ## ( Reverse process of chunking )
            
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            # chunked.draw()  ## Draws a parse tree
            print(chunked)

            '''Grouping together bunch of similar words using parts of speech '''
    except Exception as e:
        print(str(e))


processContent()
