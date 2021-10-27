from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome("C:/Users/Devil/PycharmProjects/Pushp_Autotest/Chrome/chromedriver.exe")
driver.maximize_window()
driver.get("http://mylagrolara.1wayit.com/")
print(driver.title)
time.sleep(5)

driver.get("http://casemgt.1wayit.com/#/login")
print(driver.title)
time.sleep(5)

driver.back()
print(driver.title)
time.sleep(5)

driver.forward()
print(driver.title)
time.sleep(5)
driver.quit()