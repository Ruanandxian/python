from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages=set()
def getLinks(pageurl):
	global pages
	html=urlopen('https://en.wikipedia.org/'+pageurl)
	bs0bj=BeautifulSoup(html,'lxml')
	try:
		print(bs0bj.get_text())
		print(bs0bj.find(id='mw-content-text').findAll("p")[0])
		print(bs0bj.find(id='ca-edit').find('span').find('a').attrs['href'])
	except AttributeError:
		print('yi xie cuo wu ,mei guan xi le')


	for link in bs0bj.findAll('a',href=re.compile('^(/wiki/)')):
		if 'href' in link.attrs:
			if link.attrs['href']  not in pages:
				new=link.attrs['href']
				print('---------------------\n'+new)
				pages.add(new)
				getLinks(new)
getLinks('')
