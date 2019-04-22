from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
i=1
while i<=100:
    html=urlopen('http://192.168.254.178/(h3zo3m451edpdtihegov0t55)/default2.aspx')
    bsObj=BeautifulSoup(html,'lxml')
    tu=bsObj.find('img',{'id':'icode'})['src']
    tu='http://192.168.254.178/(lyuiqz553kcsxrq5np242f45)/'+tu
    urlretrieve(tu,'C:/Users/A/Desktop/123/'+str(i)+'.gif')
    i+=1

