from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer


ps = PorterStemmer()

example = "Hello this is helpful Awsaf, helping the people who are helpless and wanting to be helped :p"

words = word_tokenize(example)

for w in words:
    print(ps.stem(w))