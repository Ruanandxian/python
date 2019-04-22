from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pymysql
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='1204628226',db='mysql',charset='utf8')
cur=conn.cursor()
cur.execute('use wikipedia')
def insertpageifnotexists(url):
    cur.execute('select * from pages where url=%s',(url))#寻找url
    if cur.rowcount==0:#如果上边没有找到，即url不在数据库中
        cur.execute('insert into pages (url) values(%s)',(url))#插入url到数据库中
        conn.commit()#提交数据库的插入操作
        return cur.lastrowid#返回刚刚操作的Id数
    return cur.fetchone()[0]#返回一条数据的第一个元素，即id
def insertlink(fromPageId,toPageId):
    cur.execute('select * from links where fromPageId=%s and toPageId=%s',(int(fromPageId),int(toPageId)))
    if cur.rowcount==0:
        cur.execute('insert into links (fromPageId,toPageId) values (%s,%s)',(int(fromPageId),int(toPageId)))
        conn.commit()
pages=set()
def getLinks(pageurl,recursionlevel):
    global pages
    if recursionlevel>4:
        return;
    pageid=insertpageifnotexists(pageurl)#获取一个主页面的id
    html=urlopen('http://en.wikipedia.org'+pageurl)
    bs0bj=BeautifulSoup(html,'lxml')
    for link in bs0bj.findAll('a',href=re.compile('^(/wiki/)((?!:).*$)')):
        insertlink(pageid,insertpageifnotexists(link.attrs['href']))#links插入对应的链接数
        if link.attrs['href'] is not pages:#加入新的url
            newpage=link.attrs['href']
            pages.add(newpage)
            getLinks(newpage,recursionlevel+1)
getLinks('/wiki/Kevin_Bacon',0)
cur.close()
conn.close()
