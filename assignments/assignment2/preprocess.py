import nltk
import random

f = open('../../data/alice_in_wonderland.txt', 'r')

text = f.read().decode('utf-8').lower()
sentences = nltk.sent_tokenize(text)

noOfSentences = len(sentences)


tokens = nltk.word_tokenize(text)
v= []
stopwords = ['!', ',', ';', '?', '.', '-', '!', '*']
for token in tokens:
    if token not in stopwords:
        v.append(token)


vocabulary = list(set(v))
v_ = [ nltk.word_tokenize(sentences[i]) for i in xrange(noOfSentences) ]



l = []

for i in xrange(noOfSentences):
    sent = v_[i]
    r = ['<s>']
    for j in xrange(len(sent)):
        if sent[j] not in stopwords:
            r.append(sent[j])
    r.append('</s>')
    l.append(r)
    

sentences = l[:100]
noOfSentences = len(sentences)



trainingData_no = int(noOfSentences*0.8)

trainingData = []
testingData = []

random.shuffle(sentences)

continous_text = []
for i in xrange(trainingData_no):
    trainingData.append(sentences[i])
    continous_text.extend(sentences[i])
for i in xrange(trainingData_no, noOfSentences):
    testingData.append(sentences[i])


__exports__ = [vocabulary, continous_text, trainingData, testingData]

