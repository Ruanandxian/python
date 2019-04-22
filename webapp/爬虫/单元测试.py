from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.PhantomJS(executable_path='C:/more/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get('http://pythonscraping.com/pages/files/form.html')
firstnameField=driver.find_element_by_name('firstname')
lastnameField=driver.find_element_by_name('lastname')
submit=driver.find_element_by_id('submit')

#1
firstnameField.send_keys('ryan')#输入
lastnameField.send_keys('michell')#输入
submit.click()#点击

#2
actions=ActionChains(driver).click(firstnameField).send_keys('ryan').click(lastnameField).send_keys('michell').send_keys(Keys.RETURN)
actions.perform()


print(driver.find_element_by_tag_name('body').text)
driver.close()