import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select

driver= webdriver.Chrome("C:/Users/QA/Pyhton_project/Pushp_Autotest/Chrome/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://landingspot.1wayit.com/")
time.sleep(3)
driver.find_element_by_xpath("//div[@class='form-group form-group-feedback form-group-feedback-left']/input[1]").send_keys("admin@averplanning.com")
driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/div[3]/input").send_keys("admin786")
driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/div[4]/button").click()
Count = driver.find_elements_by_xpath("//select[@class='select2-hidden-accessible']/option")
Count = len(Count)
print(Count)
selct= Select(driver.find_element_by_xpath("//select[@class='select2-hidden-accessible']"))
NumOfClicks = driver.find_element_by_xpath("//div[@id='tracking_listing_paginate']/span/a[last()]").text
NumOfClicks = int(NumOfClicks)
print(NumOfClicks)
for i in range (Count):
     driver.execute_script("window.scroll(0, 0);")
     selct.select_by_index(i)
     time.sleep(3)

    # # Count no. of rows
     for ii in range(NumOfClicks-1):
        driver.execute_script("window.scroll(0, 0);")
        rowx= "/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div[5]/div[2]/div/table/tbody/tr"
        rowx= len(driver.find_elements_by_xpath(rowx))
        driver.find_element_by_xpath("//div[@id='tracking_listing_paginate']/a[2]").click()
        time.sleep(0.5)
     driver.refresh()



    #driver.quit()

    # for i in range(1,rowx+1):
    #     for j in range(1,colx+1):
    #         element = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div[5]/div[2]/div/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
    #         print(element,end= '   ' )
    #     print()