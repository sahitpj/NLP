from nltk.tokenize import word_tokenize
from collections import Counter

f = open('../data/tom_sawyer.txt')
l = f.readlines()

stopWords = ['.', ',', '!', '?']
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
text_in_words = [i for i in word_tokenize(data.lower()) if i not in stopWords]
count = Counter(text_in_words)

print count


        
