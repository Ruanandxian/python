# encoding=utf8
import time
from selenium import webdriver

phone='18568670217'


browser = webdriver.PhantomJS(executable_path='C:/more/phantomjs-2.1.1-windows/bin/phantomjs.exe')
browser.implicitly_wait(8)
browser.get('http://reg.ztgame.com/')
browser.find_element_by_xpath('//*[@id="reg_form"]/div[1]/input').send_keys(phone)
browser.find_element_by_xpath('//*[@id="reg_form"]/div[2]/input[2]').click()
browser.quit()