from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver=webdriver.PhantomJS(executable_path='C:/more/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)#显示等待
print(driver.find_element_by_id('content').text)
#driver.close()


pageSource=driver.page_source
bsObj=BeautifulSoup(pageSource)
print(bsObj.find(id='content').get_text())
driver.close()
