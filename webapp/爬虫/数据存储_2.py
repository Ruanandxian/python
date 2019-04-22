from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'


def getAbsoluteURL(baseUrl, source):
	if source.startswith("http://www."):
		url = "http://"+source[11:]
	elif source.startswith("http://"):
		url = source
	elif source.startswith("www."):
		url = source[4:]
		url = "http://" + source
	else:
		url = baseUrl + "/" + source
		if baseUrl not in url:
			#print(baseUrl)
			return None
	return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
	path = absoluteUrl.replace("www.", "")
	path = path.replace(baseUrl, "")
	print(path)#/img/lrg%20(1).jpg
	path = downloadDirectory + path
	print(path)#downloaded/img/lrg%20(1).jpg
	directory = os.path.dirname(path)
	print(directory)#downloaded/img
	if not os.path.exists(directory):
		os.makedirs(directory)
	return path

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html,'lxml')
downloadList = bsObj.findAll(src=True)
for download in downloadList:
	fileUrl = getAbsoluteURL(baseUrl, download["src"])
	if fileUrl is not None:
		print(fileUrl)
print(fileUrl)
urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
