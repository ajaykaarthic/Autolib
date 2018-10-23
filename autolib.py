import json
from selenium import webdriver
import time

# Path of chromedriver for selenium
driver = webdriver.Chrome("chromedriver.exe")
url = 'http://192.168.6.70/LOGIN.ASP'
driver.get(url)

driver.find_element_by_name('user_id').send_keys("2016IT0540")  
driver.find_element_by_name('pwd').send_keys("bits")  
driver.find_element_by_name('log').click()
driver.find_element_by_xpath('//a[@href="issueresult.asp"]').click()
driver.find_element_by_name('87035b').click()
driver.find_element_by_name('87596b').click()
driver.find_element_by_name('93437b').click()
driver.find_element_by_name('b1').click()
driver.switch_to_alert().accept();



				
