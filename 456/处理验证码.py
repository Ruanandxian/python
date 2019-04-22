from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image
import cv2
import numpy as np
i=1
while i<=100:
    html=urlopen('http://192.168.254.178/(h3zo3m451edpdtihegov0t55)/default2.aspx')
    bsObj=BeautifulSoup(html,'lxml')
    tu=bsObj.find('img',{'id':'icode'})['src']
    tu='http://192.168.254.178/(lyuiqz553kcsxrq5np242f45)/'+tu
    urlretrieve(tu,'C:/Users/A/Desktop/123/'+str(i)+'.gif')
    im = Image.open('C:/Users/A/Desktop/123/'+str(i)+'.gif')
    #im1 = im.convert('L')
    im.save('C:/Users/A/Desktop/1234/'+str(i)+'.bmp')
    img = cv2.imread('C:/Users/A/Desktop/1234/'+str(i)+'.bmp', 0)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    closed = cv2.morphologyEx(img,cv2.MORPH_CLOSE, kernel)
    cv2.imwrite('C:/Users/A/Desktop/1234/'+str(i)+'.bmp',closed)
    i+=1

