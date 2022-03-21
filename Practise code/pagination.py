import time

from selenium import webdriver

driver= webdriver.Chrome("C:/Users/QA/Pyhton_project/Pushp_Autotest/Chrome/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://averreplica.1wayit.com/")
time.sleep(3)
driver.find_element_by_xpath("//div[@class='form-group form-group-feedback form-group-feedback-left']/input[1]").send_keys("admin@averplanning.com")
driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/div[3]/input").send_keys("admin786")
driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/div[4]/button").click()

time.sleep(3)

driver.quit()