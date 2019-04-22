from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from PIL import Image
import cv2
import subprocess
import requests
import time
import numpy as np

#获取验证码并清洗
#yonghu=BeautifulSoup.find('input',{'name':'txtUserName'})['value']
html = urlopen('http://192.168.254.178/(h3zo3m451edpdtihegov0t55)/default2.aspx')
bsObj = BeautifulSoup(html, 'lxml')
tu = bsObj.find('img', {'id': 'icode'})['src']
tu = 'http://192.168.254.178/(lyuiqz553kcsxrq5np242f45)/' + tu
urlretrieve(tu, '1.gif')
im = Image.open('1.gif')
# im1 = im.convert('L')
im.save('1.bmp')
img = cv2.imread('1.bmp', 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('1.bmp', closed)
p = subprocess.Popen(['tesseract', '1.bmp', '1', '-l', 'my'], stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
p.wait()
f=open('1.txt','r')
captchaResponse = f.read().replace(' ', '').replace('\n', '')
print('验证码是：' + captchaResponse)


if len(captchaResponse)==4:
    html=urlopen('http://query.hrxy.edu.cn/(S(wozpsiqqegbpvh45vgc4vq45))/default2.aspx')
    bsObj=BeautifulSoup(html,'lxml')
    formBuildId = bsObj.find('input', {'name': '__VIEWSTATE'})['value']
    print(formBuildId)
    captchaSid = bsObj.find('input', {'name': '__EVENTVALIDATION'})['value']
    print(captchaSid)
    tou={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

    params = {'__VIEWSTATE':formBuildId,'__EVENTVALIDATION':captchaSid,'txtUserName': '17104020058', 'TextBox2':'woaixiaoruan2728','txtSecretCode':captchaResponse,'RadioButtonList1':'(unable to decode value)'}
    r=requests.post('http://query.hrxy.edu.cn/(S(jrjb1v45ujcortb43fq3wrve))/default2.aspx',data=params,headers=tou)
    time.sleep(5)
    responseObj=BeautifulSoup(r.text,'lxml')
    if responseObj.find('title') is not None:
        print(responseObj.find('title').get_text())

