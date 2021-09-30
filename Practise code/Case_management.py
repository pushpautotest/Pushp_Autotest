import time

from selenium import webdriver
driver= webdriver.Chrome("C:/Users/crochet/PycharmProjects/Pushp_Autotest/Chrome/chromedriver.exe")

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://casemgt.1wayit.com/#/login")

#Locating Elements
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[1]/form/div[1]/input").send_keys("pushpender1wayit@gmail.com")
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[1]/form/div[2]/input").send_keys("12345678")
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[1]/form/div[4]/input") .click()
for i in range(2,9):
    driver.find_element_by_xpath("/html/body/app-root/div[2]/ul/li["+str(i)+"]/a").click()
    time.sleep(5)
driver.quit()