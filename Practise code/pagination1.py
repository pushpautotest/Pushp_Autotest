from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
driver= webdriver.Chrome("C:/Users/QA/Pyhton_project/Pushp_Autotest/Chrome/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://landingspot.1wayit.com/login")
driver.find_element_by_xpath("")
