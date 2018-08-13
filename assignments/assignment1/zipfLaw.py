import loader
from nltk.corpus import wordnet as wn
import matplotlib.pyplot as plt
import random
import math

print math.log(10)

textInWords = loader.loader("dataCollection")[1]
Ranks = loader.loader("dataCollection")[2]
wordFrequencies = loader.loader("dataCollection")[3]

randints = [random.randint(0, 8000) for i in xrange(10)]
testWords = sorted([ textInWords[randints[i]] for i in xrange(10)])
wordRanks = [ Ranks[randints[i]] for i in xrange(10)]

noOfWordMeanings = [ len(wn.synsets(testWords[i])) for i in xrange(10)]
wordLength = [ len(testWords[i]) for i in xrange(10)]
wordFrequencies = [ wordFrequencies[randints[i]] for i in xrange(10)]

logOfWordRanks = []
logOfWordFrequencies = []
logOfWordLength = []
logWordMeanings = []



for i in xrange(10):
    if noOfWordMeanings[i] == 0:
        noOfWordMeanings[i] = 1
    logOfWordFrequencies.append(math.log(float(wordRanks[i])))
    logOfWordLength.append(math.log(float(wordLength[i])))
    logOfWordRanks.append(math.log(float(wordRanks[i])))
    logWordMeanings.append(math.log(float(noOfWordMeanings[i])))



plt.plot(logWordMeanings,logOfWordRanks, 'r', '-')
plt.plot(logWordMeanings, logOfWordFrequencies, 'b', '-.-')
plt.plot(logOfWordLength, logOfWordFrequencies, 'g')
plt.plot(logOfWordLength, logOfWordRanks, 'c')
plt.show()

lVSf = [ wordFrequencies[i]*wordLength[i] for i in xrange(10)]
lVSr = [ wordRanks[i]/float(wordLength[i]) for i in xrange(10)]
mVSf = [ math.sqrt(wordFrequencies[i])/float(noOfWordMeanings[i]) for i in xrange(10)]
mVSr = [ math.sqrt(wordRanks[i])*float(noOfWordMeanings[i]) for i in xrange(10)]
