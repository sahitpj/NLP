import loader
import matplotlib.pyplot as plt


textInWords = loader.loader('dataCollection')[0]

dataPoints_x = []
dataPoints_y = []
for i in xrange(10):
    splitList = textInWords[0: (i+1)*9000]
    uniqueWords = len(list(set(splitList)))
    dataPoints_x.append(uniqueWords)
    dataPoints_y.append((i+1)*9000)

plt.plot(dataPoints_y, dataPoints_x)
plt.show()




