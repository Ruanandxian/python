from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import string


def cleanInput(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]', '', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'utf-8')
    input = input.decode('ascii', 'ignore')
    # input=input.upper()
    output = []
    input = input.split(' ')
    for i in input:
        i = i.strip(string.punctuation)  # 去除所有的标点符号,string.punctuation为查看所有的标点符号
        if len(i) > 1 or (i.lower() == 'a' or i.lower() == 'i'):
            output.append(i)
    return output


def ngrams(input, n):
    input = cleanInput(input)
    #   print(input)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output


html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, 'lxml')
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
ngram = ngrams(content, 2)
#ngram = OrderedDict(sorted(ngram.items(), key=lambda t: t[1], reversed=True))  # 排序,[()],{}，list，才可以使用
print(ngram)
print('2-gram count is:' + str(len(ngram)))
