from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('http://www.hrxy.com/')
bsobj=BeautifulSoup(html.read(),'lxml')
print(bsobj.body)