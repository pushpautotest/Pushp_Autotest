from selenium import webdriver
driver= webdriver.Chrome("C:/Users/QA/Pyhton_project/Pushp_Autotest/Chrome/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.mylagro.com/")
driver.find_element_by_xpath("//div/nav/div/ul[2]/li[3]").click()
time.sleep(10)
driver.quit()