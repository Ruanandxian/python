from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import requests
j=0
url='http://www.mzitu.com/page/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
#main_page=requests.get(url,headers=headers)
#print(main_page.text)
def jia(referer):
    headers['Referer']='{}'.format(referer)
shu=4
for i in range(1,int(shu)):
    new_url=url+str(i)
    new_page=requests.get(new_url,headers=headers)
    bsObj=BeautifulSoup(new_page.text,'html.parser')
    links=bsObj.find(id='pins').findAll('a',target='_blank')[1::2]
    for link in links:
        link=link['href']
        soup=BeautifulSoup(requests.get(link,headers=headers).text,'html.parser')
        tu=soup.find('div',class_='pagenavi').findAll('a')[4].get_text()
        for i in range(1,int(tu)):
            sss=link+'/'+str(i)
            jia(sss)
            xia=requests.get(sss,headers=headers)
            xiazai=BeautifulSoup(xia.text,'html.parser')
            emmm=xiazai.find('div','main-image').find('img')['src']
            print(emmm)
            emmm_name=emmm.split('/')[-1]
            f = open('C:/Users/A/Desktop/emmm/' + str(emmm_name), 'wb')
            f.write(requests.get(emmm, headers=headers).content)
            f.close()
print('en')