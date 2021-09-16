import time

from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:\\Users\\Devil\\Desktop\\chromedriver_win32\\chromedriver.exe")
#driver =webdriver.Chrome('https://www.google.com/')
driver.maximize_window()
driver.get("http://mylagrolara.1wayit.com")
print("Executed successfully")
#driver.get_element_by_xpath("//div/")
time.sleep(5)
driver.quit()
