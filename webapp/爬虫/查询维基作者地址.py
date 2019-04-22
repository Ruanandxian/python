from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import json
random.seed(datetime.datetime.now())
def getLinks(url):
	html=urlopen('http://en.wikipedia.org'+url)
	bs0bj=BeautifulSoup(html,'lxml')
	compile=bs0bj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))
	return compile

def getHist(url):
	url=url.replace('/wiki/','')
	pageurl='http://en.wikipedia.org/w/index.php?title='+url+'&action=history'
	print('history url is:'+pageurl)
	html=urlopen(pageurl)
	bs0bj=BeautifulSoup(html,'lxml')
	ip=bs0bj.findAll('a',{'class':'mw-anonuserlink'})
	ipadress=set()
	for i in ip:
		ipadress.add(i.get_text())
	return ipadress
def getCountry(ip):
		response=urlopen('http://api.ipstack.com/'+ip+'?access_key=d65b8aa4d1fa4b2a4eac0780f2286a2c').read().decode('utf-8')
		responseJson=json.loads(response)
		return responseJson.get('country_code')
links=getLinks('/wiki/Python_(programming_language)')

while(len(links)>0):
	for link in links:
		print('---------------------------------')
		history=getHist(link.attrs['href'])
		for i in history:
			country=getCountry(i)
			if country is not None:
				print(i+' is from ['+country+']')

	new=links[random.randint(0,len(links)-1)].attrs['href']
	links=getLinks(new)