from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages=set()
def getLinks(url):
	global pages
	html=urlopen('https://en.wikipedia.org/'+url)
	bs0bj=BeautifulSoup(html,'lxml')
	for link in bs0bj.findAll('a',href=re.compile('^(/wiki/)')):#link实际是一个一个进行的
		if link.attrs['href'] not in pages:
			new=link.attrs['href']
			print(new)
			pages.add(new)
			getLinks(new)#递归爬取二级网站的链接，逐步深入
getLinks('')
#/wiki/Wikipedia
#{'/wiki/Wikipedia'}
#/wiki/Free_content
#{'/wiki/Wikipedia', '/wiki/Free_content'}
#/wiki/Encyclopedia
#{'/wiki/Encyclopedia', '/wiki/Wikipedia', '/wiki/Free_content'}