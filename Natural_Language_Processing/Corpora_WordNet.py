import nltk

from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize,word_tokenize

synnonyms = wordnet.synsets("program")


print(synnonyms)
print(synnonyms[0].name()) # first syn - synset
print(synnonyms[0].lemmas()[0].name()) # name of syn

print(synnonyms[0].definition()) # first syn - definition
print(synnonyms[0].examples()) # first syn - Examples

synno = []
anto = []

print("Getting Synnonyms and Antonyms ----------")
for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        # print(l) ## All possible lemmas
        synno.append(l.name())
        if l.antonyms():
            anto.append(l.antonyms()[0].name())

print(set(synno))
print(set(anto))

print("----- Semantic Similarity -----")

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2)) ## Gives the percentage similarity

print("----- Semantic Similarity -----")
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print(w1.wup_similarity(w2)) ## Gives the percentage similarity

print("----- Semantic Similarity -----")
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cat.n.01")
print(w1.wup_similarity(w2)) ## Gives the percentage similarity

print("----- Semantic Similarity -----")
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cactus.n.01")
print(w1.wup_similarity(w2)) ## Gives the percentage similarity

## a ship is more similar to a cactus than a cat :o :o
