import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.tag import pos_tag
from nltk.stem import PorterStemmer

notFoundWordsSimilar = []
ps = PorterStemmer()

def findMisspell(sentence):
    count = 0
    mispelled = set()


    for x in sentence:
        if not x in mispelled:

            match = findMatch(x)

            if match == "":
                #print('Mispelled word is ', x, ' and it was not found in the text')
                mispelled.add(x)
                #count+=1
                #print(count, x)

    return mispelled

def findMatch(word):

    if word.lower() in words:
            return word;
    if word.isnumeric():
        return "11"

    if not word.isalpha():
        return "111"
    stemmed = ps.stem(word)
    if not stemmed == word:
        return word

    return ""


def findMatch2(word):

    if word.lower() in words:
        return word;

    return ""

def editDistance(word):
    #print(word, ' is in editDistance')
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    space = ' '
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def findReplacements(mispelled):
    total = 0
    myList = []
    for i in mispelled:
        replacesConfirmed = []
        replaces = editDistance(i)
        for x in replaces:
            match = findMatch2(x)
            if match != "":
                replacesConfirmed.append(x)
                if len(replacesConfirmed) > 2:
                    broke = 1
                    break

        #print(len(replaces))
        counter = 0
        while counter < 2 and len(replacesConfirmed) < 2:
            #print('infitnie loop')
            total +=1
            for x in replaces:
                replaces2 = editDistance(x)
                if len(replacesConfirmed) > 2:
                    break
                for xx in replaces2:
                    match = findMatch2(xx)
                    if match != "":
                        replacesConfirmed.append(xx)
                        if len(replacesConfirmed) > 2:
                            break
            replaces = replaces2
            counter += 1

        if len(replacesConfirmed) == 0:
            replacesConfirmed.append('No simliar words found')
        print (i, ': %s' % ', '.join(map(str, replacesConfirmed)))





        #print (i, ': %s' % ', '.join(map(str, replacesConfirmed)))


        myList.append(replacesConfirmed)

        #myList.append(replacesConfirmed)
        #print('\n')
    return myList
#f = open("mobydick.txt", 'r')
f = open("english3.txt", 'r')
data = f.readlines()
newdata = list()
for x in data: # smart, collection and iterator savvy
    x = x.strip() # no semicolons YAY! mandatory intendations YAY!
    newdata.append(x)
#print(newdata)
corpus = "\n".join(data)
#print(corpus);
words = set()
wordsList = word_tokenize(corpus)
for i in wordsList:
    words.add(i)



#print(words[1:100])

fs = open("mobydick.txt", 'r')
data1 = fs.readlines()

#print(data)
newdata1 = list()
for x in data1: # smart, collection and iterator savvy
    x = x.strip() # no semicolons YAY! mandatory intendations YAY!
    newdata1.append(x)
#print(newdata)
corpus1 = "\n".join(data1)
#print(corpus);

words1 = wordpunct_tokenize(corpus1)
pos_tagged = pos_tag(words1)
#print(pos_tagged[1:100])
propernouns = [word for word,pos in pos_tagged if pos == 'NNP']
#print(propernouns)

#myString = input("Enter your sentence: ")
#print(myString)
#myStringWords =  word_tokenize(myString)
#print(myStringWords);

mispelled = findMisspell(words1)
#print(mispelled[1:100])
#print(len(mispelled))
#print(mispelled)
reps = findReplacements(mispelled)
