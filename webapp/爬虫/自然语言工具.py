from nltk import sent_tokenize#对文本按照句子进行分割
from nltk import word_tokenize#对句子进行分词
from nltk import Text
from nltk.book import *
from nltk import FreqDist#查询单词使用频率
from nltk import bigrams#2-gram模型
from nltk import ngrams#n-gram模型，一般情况下
from nltk import pos_tag#识别每个单词的词性

word=word_tokenize('my and and and ...')
print(word)

fdist=FreqDist(text6)
print(fdist.most_common(10))#大于10次单词的频率，从大到小排列
print(fdist['Grail'])#查询单词出现了多少次


bigrams=bigrams(text6)
bigramsDist=FreqDist(bigrams)
print(bigramsDist)#<FreqDist with 7349 samples and 16966 outcomes>
print(bigramsDist[('Sir','Robin')])#2gram模型


fourgrams=ngrams(text6,4)
fourgramsDist=FreqDist(fourgrams)
#print(fourgramsDist)
print(fourgramsDist.most_common(10))#统计4-gram模型出现的次数
print(fourgramsDist[('father','smelt','of','elderberries')])#查询指定单词出现的次数


tests=ngrams(text6,4)#循环打印出以coconut开头的4-gram
for test in tests:
    if test[0]=='coconut':
        print(test)


text=word_tokenize('The dust was thick so he had to dust')
print(pos_tag(text))#查看词性