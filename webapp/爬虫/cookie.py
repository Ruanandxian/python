from selenium import webdriver
drive=webdriver.PhantomJS(executable_path='C:/more/phantomjs-2.1.1-windows/bin/phantomjs.exe')
drive.get('http://pythonscraping.com')
drive.implicitly_wait(1)
print(drive.get_cookies())

saveCookies=drive.get_cookies()

driver=webdriver.PhantomJS(executable_path='C:/more/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get('http://pythonscraping.com')#得到cookie
driver.delete_all_cookies()#删除所有cookie
for cookie in saveCookies:
    driver.add_cookie(cookie)#一个个添加cookie

driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print(driver.get_cookies())
