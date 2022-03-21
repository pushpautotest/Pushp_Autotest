import time

from selenium import webdriver

driver= webdriver.Chrome("C:/Users/QA/Pyhton_project/Pushp_Autotest/Chrome/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://landingspot.1wayit.com/login")
driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/div[2]/input").send_keys("pushp@yopmail.com")
driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/div[3]/input").send_keys(12345678)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/div[4]/button").click()
title = []
for i in range (1,10):
 time.sleep(2)
 if i == 3:
  continue
 driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/li["+str(i)+"]/a").click()
 name = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div/div/h2").text
 title.append(name)
print (title)
time.sleep(5)
driver.quit()