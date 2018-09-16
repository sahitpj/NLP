import loader


data = loader.loader('preprocess')

vocabulary = data[0]
continous_text = data[1]
trainData = data[2]
testData = data[3]

#Test1

#print vocabulary[2:20]
#print continous_text[2:20]
#print trainData[2:20]
#print testData[2:20]

'''
Test1 passed
'''


#Test2

from models import language_model, sentence_model

#bring in the language_model and the sentence_model

'''
Test2 passed
'''

#Test3
#initialising objects

lang_model = language_model(continous_text, vocabulary)
sent_model = sentence_model(continous_text, vocabulary, language_model)

'''
Test3 passed
'''

#Test4

#chechking all functions for language_model

#lang_model.unigram_count_cal()
#lang_model.bigram_count_cal()
#.unigram_model
#.bigram_model
#.trigram_model
#.quadgram_model


'''
Test4 passed
'''

#Test5

#checking all functions for sentence_model

# print testData[4]
# l = ['<s>', u'oh', u'dear', '</s>'] 
# print sent_model.sentence_prob(l, None, "unigram")
# print sent_model.sentence_prob(l, None, "quadgram")
# print sent_model.sentence_generator("quadgram", None)
# print sent_model.bigram_perplexity( testData[3], None)

'''
Test5 passed
'''