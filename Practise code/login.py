from selenium import webdriver
import time
import string
import random
driver= webdriver.Chrome("C:/Users/QA/Pyhton_project/Pushp_Autotest/Chrome/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.mylagro.com/")
driver.find_element_by_xpath("//div/nav/div/ul[2]/li[3]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[1]/div/i[2]").click()
time.sleep(5)

a = "@yopmail.com"
lenth = 10
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = lenth))
print(str(res) + a)
c = str(res) + a
# print(c)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[1]/div/input").send_keys(c)

psw = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = lenth))
d = str(psw)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[2]/div/input").send_keys(d)

print(d)


#
time.sleep(10)
#
#
#
#
# # print("The generated random string : " + str(res))
#
driver.quit()