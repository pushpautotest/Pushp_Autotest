import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select

driver= webdriver.Chrome("C:/Users/QA/Pyhton_project/Pushp_Autotest/Chrome/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://averreplica.1wayit.com/")
time.sleep(3)
driver.find_element_by_xpath("//div[@class='form-group form-group-feedback form-group-feedback-left']/input[1]").send_keys("admin@averplanning.com")
driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/div[3]/input").send_keys("admin786")
driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/div[4]/button").click()
Count = driver.find_elements_by_xpath("//select[@class='select2-hidden-accessible']/option")
Count = int(len(Count))
# print(int(Count))
selct= Select(driver.find_element_by_xpath("//select[@class='select2-hidden-accessible']"))
for i in range (0,Count):
    selct.select_by_index(i)

    # Getting the no. of pages
    element= driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div[5]/div[2]/div/div[4]").text
    a= element.index('of')
    s= element[a+7:]
    print(s)

    # # Count no. of rows
    # rowx= "/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div[5]/div[2]/div/table/tbody/tr"
    # rowx= len(driver.find_elements_by_xpath(rowx))
    # # Count no. of Columns
    # colx= "/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div[5]/div[2]/div/table/tbody/tr[1]/td"
    # colx= len(driver.find_elements_by_xpath(colx))
    # print("No. of rows in table:  ", rowx)
    # print("No. of Columns in table:  ", colx)


    driver.quit()

    # for i in range(1,rowx+1):
    #     for j in range(1,colx+1):
    #         element = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div[5]/div[2]/div/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
    #         print(element,end= '   ' )
    #     print()