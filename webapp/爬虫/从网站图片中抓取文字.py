import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver
driver=webdriver.PhantomJS(executable_path='C:/more/phantomjs-2.1.1-windows/bin/phantomjs.exe')
#driver=webdriver.Firefox()
driver.get('https://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200')
time.sleep(3)
driver.find_element_by_id('sitbLogoImg').click()#点击
imageList=set()
time.sleep(5)

#当向右箭头可以点击时，开始翻页
while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    #获取已加载的新页面
    pages=driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image=page.get_attribute('src')
        imageList.add(image)
    driver.quit()

for image in sorted(imageList):
    urlretrieve(image,'page.jgp')
    p=subprocess.Popen(['tesseract','page,jpg','page'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    f=open('page.txt','r')
    print(f.read())