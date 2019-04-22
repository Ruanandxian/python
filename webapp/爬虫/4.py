from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsobj=BeautifulSoup(html.read(),'lxml')
namelist=bsobj.findAll('span',{'class':{'green','red'}})#打印红色和绿色的文字

#name=bsobj.findAll(text='the prince')
#print(len(name))#打印文中the prince的数量

for name in namelist:
	print(name.get_text())
	#只打印文字