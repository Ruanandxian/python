from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
pages=set()
random.seed(datetime.datetime.now())

#获取页面所有内链列表
def getInternalLinks(bs0bj,includeUrl):
	internalLinks=[]
	#找出所有以'/'开头的链接
	for link in bs0bj.findAll('a',href=re.compile('^(/|.*'+includeUrl+')')):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks

#获取页面所有的外链的列表
def getExternalLinks(bs0bj,excludeUrl):
	getExternalLinks=[]
	#找出所有以http或www开头的外链并且不包含当前的url链接
	for link in bs0bj.findAll('a',href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in getExternalLinks:
				getExternalLinks.append(link.attrs['href'])
	return getExternalLinks

def splitAddress(address):
	#作用是去除一个链接的http://和以/来分割
	addressParts=address.replace('http://','').split('/')
	return addressParts

def getRandomExternalLink(startingPage):
	html=urlopen(startingPage)
	bs0bj=BeautifulSoup(html,'lxml')
	externalLinks=getExternalLinks(bs0bj,splitAddress(startingPage)[0])
	if len(externalLinks)==0:
		internalLinks=getInternalLinks(startingPage)
		return getExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
	externalLink=getRandomExternalLink('http://oreilly.com')
	print('随机外链是：'+externalLink)
	followExternalOnly(externalLink)

#followExternalOnly('http://oreilly.com')

allExtlinks=set()
allIntlinks=set()
def getAllExternalLinks(siteUrl):
	html=urlopen(siteUrl)
	bs0bj=BeautifulSoup(html,'lxml')
	internalLinks=getInternalLinks(bs0bj,splitAddress(siteUrl)[0])
	externalLinks=getExternalLinks(bs0bj,splitAddress(siteUrl)[0])
	for link in externalLinks:
		if link not in allExtlinks:
			allExtlinks.add(link)
			print(link)
	for link in internalLinks:
		if link not in allIntlinks:
			print('即将获取链接的url是：'+link)
			allIntlinks.add(link)
			getAllExternalLinks(link)

getAllExternalLinks('http://oreilly.com')