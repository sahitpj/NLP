from nltk.tokenize import word_tokenize
from collections import Counter


f = open('../../data/tom_sawyer.txt')
l = f.readlines()

stopWords = ['.', ',', '!', '?', '-', ';', '_']
def lineCorrector(l):
    p = l[:-2]
    if len(p) > 0:
        return p
lines_ = map(lineCorrector, l)
lines = []
for i in lines_:
    if i != None:
        lines.append(i)

lines = lines[252:]
data = ' '.join(lines).decode('utf-8')
textInWords = [i for i in word_tokenize(data.lower()) if i not in stopWords]
count = Counter(textInWords)
wordFrequencies = sorted(count.values(), reverse=True)


sortedTypes =  sorted(count.items(), key=lambda i: i[1], reverse=True)
tokens = word_tokenize(data.lower())
types = [ sortedTypes[j][0] for j in xrange(len(sortedTypes)) ]
Ranks = []

noOfTokens = float(len(tokens))
noOfTypes = float(len(types))
TTR = noOfTypes/noOfTokens


for i in xrange(int(noOfTypes)):
    if i == 0:
        Ranks.append(i+1)
    else:
        if wordFrequencies[i-1] == wordFrequencies[i]:
            Ranks.append(Ranks[-1])
        else:
            Ranks.append(Ranks[-1]+1)

__exports__ = [textInWords, types, Ranks, wordFrequencies]


