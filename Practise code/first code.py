import time

from selenium import webdriver

driver= webdriver.Chrome("C:/Users/Devil/PycharmProjects/pythonProject/Chrome/chromedriver.exe")
#driver =webdriver.Chrome('https://www.google.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://mylagrolara.1wayit.com")
#print("Executed successfully")
#driver.get_element_by_xpath("//div/")

driver.find_element_by_xpath("//*[@id='navbarsExample09']/ul[2]/li[3]/a") .click()
#time.sleep(5)
driver.find_element_by_xpath("//*[@id='login']/div/div/div/div/div[2]/div[2]/div/form/div[1]/div/i[2]") .click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='login']/div/div/div/div/div[2]/div[2]/div/form/div[1]/div/input").send_keys("pushp@yopmail.com")
driver.find_element_by_xpath("//*[@id='login']/div/div/div/div/div[2]/div[2]/div/form/div[2]/div/input").send_keys("12345678")
driver.find_element_by_xpath("//*[@id='login']/div/div/div/div/div[2]/div[2]/div/form/div[4]/button") .click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='navbarsExample09']/ul[2]/li[3]/div") .click()
time.sleep(5)
#for i in range(1,10):
driver.find_element_by_xpath("//*[@id='navbarsExample09']/ul[2]/li[3]/div/div[2]/ul/li[1]/a") .click()
time.sleep(10)
driver.quit()
