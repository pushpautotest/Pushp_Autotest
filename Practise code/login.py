from selenium import webdriver                      #importing libraries
import time
import string
import random

#Initializing chrome
print("Test to check the login functionality with invalid loing and invalid password \n")
driver= webdriver.Chrome("C:/Users/QA/Pyhton_project/Pushp_Autotest/Chrome/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

# Entering Url
driver.get("https://www.mylagro.com/")
driver.find_element_by_xpath("//div/nav/div/ul[2]/li[3]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[1]/div/i[2]").click()
time.sleep(5)

# domain addition
a = "@yopmail.com"
lenth = 10
i=0
while i < 3:

    #username generation and domain attachment
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k = lenth))
    # print(str(res) + a)
    c = str(res) + a
    # print(c)

    # ***** Password Generation *******
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[1]/div/input").send_keys(c)
    psw = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k = lenth))
    d = str(psw)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[2]/div/input").send_keys(d)
    # print(d)
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[4]/button").click()
    time.sleep(5)
    # Getting Error message
    message = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/p[1]").text
    # validation = str(message)
    if i == 0:
        print("First Attempt Result")
        print(message)

    elif i == 1:
        print("\nSecond Attempt Result" )
        print(message)

    else:
        print(" \nThird Attempt Result ")
        print(message)

    i = i+1

# print("The generated random string : " + str(res))
driver.quit()