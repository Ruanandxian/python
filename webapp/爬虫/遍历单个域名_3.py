from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
random.seed(datetime.datetime.now())
def getLinks(url):
	html=urlopen('https://en.wikipedia.org/'+url)
	bs0bj=BeautifulSoup(html,'lxml')
	return bs0bj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))
links=getLinks('wiki/Kevin_Bacon')
while len(links)>0:
	new=links[random.randint(0,len(links)-1)].attrs['href']
	print(new)
	links=getLinks(new)