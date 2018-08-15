import loader
from nltk.corpus import wordnet as wn
import matplotlib.pyplot as plt
import random
import math


textInWords = loader.loader("dataCollection")[1]
Ranks = loader.loader("dataCollection")[2]
wordFrequencies = loader.loader("dataCollection")[3]

randints = [random.randint(0, 8000) for i in xrange(30)]
testWords = sorted([ textInWords[randints[i]] for i in xrange(30)])
wordRanks = [ Ranks[randints[i]] for i in xrange(30)]

noOfWordMeanings = [ len(wn.synsets(testWords[i])) for i in xrange(30)]
wordLength = [ len(testWords[i]) for i in xrange(30)]
wordFrequencies = [ wordFrequencies[randints[i]] for i in xrange(30)]

logOfWordRanks = []
logOfWordFrequencies = []
logOfWordLength = []
logWordMeanings = []



for i in xrange(30):
    if noOfWordMeanings[i] == 0:
        noOfWordMeanings[i] = 1
    logOfWordFrequencies.append(math.log(float(wordRanks[i])))
    logOfWordLength.append(math.log(float(wordLength[i])))
    logOfWordRanks.append(math.log(float(wordRanks[i])))
    logWordMeanings.append(math.log(float(noOfWordMeanings[i])))



plt.scatter(logOfWordFrequencies, logOfWordRanks)
plt.show()

plt.scatter(logWordMeanings,logOfWordRanks)
plt.ylim((3,10))
plt.show()

plt.scatter(logWordMeanings, logOfWordFrequencies)
plt.ylim((-10,20))
plt.show()

plt.scatter(logOfWordLength, logOfWordFrequencies)
plt.ylim((-10,20))
plt.show()

plt.scatter(logOfWordLength, logOfWordRanks)
plt.ylim((0,10))
plt.show()

lVSf = [ wordFrequencies[i]*wordLength[i] for i in xrange(30)]
lVSr = [ wordRanks[i]/float(wordLength[i]) for i in xrange(30)]
mVSf = [ math.sqrt(wordFrequencies[i])/float(noOfWordMeanings[i]) for i in xrange(30)]
mVSr = [ math.sqrt(wordRanks[i])*float(noOfWordMeanings[i]) for i in xrange(30)]

