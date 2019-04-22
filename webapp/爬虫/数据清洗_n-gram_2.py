from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator
def cleaninput(input):
    input=re.sub('\n+',' ',input)
    input=re.sub('\[[0-9]*\]','',input)
    input=re.sub(' +',' ',input)
    input=bytes(input,'utf-8')
    input=input.decode('ascii','ignore')
    cleaninput=[]
    input=input.split(' ')
    for i in input:
        i=i.strip(string.punctuation)
        if len(i)>1 or (i.lower()=='a'or i.lower()=='i'):
            cleaninput.append(i)
    return cleaninput
def ngrams(input,n):
    input=cleaninput(input)
    output={}
    for i in range(len(input)-n+1):
        ngram=' '.join(input[i:i+n])
        if ngram not in output:
            output[ngram]=0
        output[ngram]+=1
    return output
def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it",
    "i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
    "they", "is", "an", "at", "but","we", "his", "from", "that", "not",
    "by", "she", "or", "as", "what", "go", "their","can", "who", "get",
    "if", "would", "her", "all", "my", "make", "about", "know", "will",
    "as", "up", "one", "time", "has", "been", "there", "year", "so",
    "think", "when", "which", "them", "some", "me", "people", "take",
    "out", "into", "just", "see", "him", "your", "come", "could", "now",
    "than", "like", "other", "how", "then", "its", "our", "two", "more",
    "these", "want", "way", "look", "first", "also", "new", "because",
    "day", "more", "use", "no", "man", "find", "here", "thing", "give",
    "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False
connect=str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')
#connect=BeautifulSoup(connect,'lxml')
#connect=connect.find('div',{'id':'mw-content-text'}).get_text()
ngram=ngrams(connect,2)
jieguo=sorted(ngram.items(),key=operator.itemgetter(1),reverse=True)
print(jieguo)
