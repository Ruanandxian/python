from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image
from PIL import ImageOps

html=urlopen('http://query.hrxy.edu.cn/(S(nglzybjp2fqvosybnoklibya))/xs_main.aspx?xh=17104020058')
bsObj=BeautifulSoup(html,'lxml')
#收集需要处理的表单数据（包括验证码和输入字段）
if bsObj.find('title') is not None:
    print(bsObj.find('title').get_text())