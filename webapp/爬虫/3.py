from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def gettitle(url):
	try:
		html=urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsobj=BeautifulSoup(html.read(),'lxml')
		title=bsobj.html.body
	except AttributeError as e:
		return None
	return title
jieguo=gettitle('https://kyfw.12306.cn/otn/gonggao/help.html')
if jieguo== None:
	print('Title could not be found')
else:
	print(jieguo)
