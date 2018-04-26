import xml.etree.ElementTree
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# TODO
# we will have to tokenize the sentence text
# use freeling, for each entity check if its begin, inside, outside in the sentence

snow_ball = nltk.stem.SnowballStemmer('english')
stop_words = set(stopwords.words('english'))


def pairEntities(sentence, pair_id_1, pair_id_2):
    for atype in sentence.findall('entity'):
        if (atype.get('id') == pair_id_1 or atype.get('id') == pair_id_2):
            print('Id: ' + str(atype.get('id')) + ' | Type: ' + str(atype.get('type')) + ' | Text: ' + str(
                atype.get('text')) + '\n')


def sentenceEntities(sentence):
    for atype in sentence.findall('entity'):
        print('Type: ' + str(atype.get('type')) + ' | Text: ' + str(atype.get('text')) + '\n')


def analyzeText(word):
    return snow_ball.stem(word)


# need to parse for each document, then go into foreach sentence, then inside sentence, look for entity and pairs
# something get all filenames inside DrugBank folder
# stemming, tokenize, and test data, then train data into types ['brand','group'] based on the test data
# file_names = ['Abacavir', 'Mazindol', 'Ezetimibe']
file_names = ['Abacavir']
sentence_object = {}
for file in file_names:
    e = xml.etree.ElementTree.parse('DrugBank/' + file + '.xml').getroot()
    print('------------------------------------ File ' + file + '----------------------------------------------')
    for sentence in e.findall('sentence'):
        print('------------------------------------------------------------------')
        print('Id: ' + str(sentence.get('id')) + ' | Text: ' + analyzeText(str(sentence.get('text'))) + '\n')
        print(word_tokenize(str(sentence.get('text'))))
        print([i for i in sentence.get('text').lower().split() if i not in stop_words])
        sentence_object[sentence.get('id')] = {i for i in sentence.get('text').lower().split() if i not in stop_words}
        # print({sentence.get('id'): [i for i in sentence.get('text').lower().split() if i not in stop_words]})
        # print(sentence_object)
        # print('Tokenize: ' + nltk.word_tokenize(str(sentence.get('text'))) + '\n')
        print('Entities of sentence')
        print('*******************************')
        sentenceEntities(sentence)
        print('Pairs of sentence')
        print('*******************************')
        for atype in sentence.findall('pair'):
            print('Id-1: ' + str(atype.get('e1')) + ' | Id-2: ' + str(atype.get('e2')) + ' Text: ' + str(
                atype.get('text')) + '\n')
            print('****************** Pair Details **********************')
            pairEntities(sentence, atype.get('e1'), atype.get('e2'))

# i think, now we will check each tokenized sentence with words, and store features with them, all type of features
print(sentence_object)
print('At the end')
for key in sentence_object:
    print(sentence_object[key])
