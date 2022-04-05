from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:/Users/QA/Pyhton_project/Pushp_Autotest/Chrome/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

# Entering URL and login
driver.get("http://jetli.1wayit.com/admin/login")
time.sleep(3)
driver.find_element_by_id('email').send_keys("jetli@yopmail.com")
driver.find_element_by_id('password').send_keys("12345678")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_xpath("/html/body/div[2]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p").click()


# Getting the pagination option type (Records per page)
Count = driver.find_elements_by_xpath("//select[@class='custom-select custom-select-sm form-control form-control-sm']/option")
Count = len(Count)
print(Count)
selct= Select(driver.find_element_by_xpath("//select[@class='custom-select custom-select-sm form-control form-control-sm']"))

for i in range(Count):
    selct.select_by_index(i)
    time.sleep(2)

    # Getting the click count
    NumOfClicks = driver.find_element_by_xpath("//div[@id='table_data_paginate']/ul/li[last()-1]").text
    NumOfClicks = int(NumOfClicks)
    print("Number of click: ", NumOfClicks-1)
    time.sleep(1)

    # Getting the row count
    for j in range(NumOfClicks - 1):
        rowx = "/html/body/div[2]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr"
        rowx = len(driver.find_elements_by_xpath(rowx))
        print(rowx)
        driver.find_element_by_xpath("//div[@id='table_data_paginate']/ul/li[9]").click()
        time.sleep(5)





driver.quit()