from selenium import webdriver

# Path of chromedriver for selenium
driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://192.168.6.70/LOGIN.ASP')

#login
driver.find_element_by_name('user_id').send_keys("roll no")  
driver.find_element_by_name('pwd').send_keys("password")  
driver.find_element_by_name('log').click()
driver.find_element_by_xpath('//a[@href="issueresult.asp"]').click()

#renew
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
    
driver.find_element_by_name('b1').click()
driver.switch_to_alert().accept();



				
