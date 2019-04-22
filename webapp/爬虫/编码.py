from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bs0bj=BeautifulSoup(html,'lxml')
content=bs0bj.find('div',{'id':'mw-content-text'}).get_text()
content=bytes(content,'utf-8')
content=content.decode('utf-8')
print(content)
