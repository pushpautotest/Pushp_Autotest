from selenium import webdriver                      #importing libraries
import time
import string
import random
from fpdf import FPDF

#Initializing chrome
print("\n*****Test to check the login functionality with invalid login and invalid password***** \n")
driver= webdriver.Chrome("C:/Users/QA/Pyhton_project/Pushp_Autotest/Chrome/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

# Entering Url
driver.get("https://www.mylagro.com/")
driver.find_element_by_xpath("/html/body/div[10]/div/div/div/div[2]/ul/li[2]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//div/nav/div/ul[2]/li[3]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[1]/div/i[2]").click()
time.sleep(5)
#
# # domain addition
ErrorMesList=[]
a = "@yopmail.com"
lenth = 10
i=0
while i < 5:
   #username generation and domain
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = lenth))
    # print(str(res) + a)
    c = str(res) + a
    # print(c)

    # ***** Password Generation *******
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[1]/div/input").send_keys(c)
    psw = ''.join(random.choices(string.ascii_lowercase + string.digits, k = lenth))
    d = str(psw)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[2]/div/input").send_keys(d)
    # print(d)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[4]/button").click()
    time.sleep(2)
    # Getting Error message
    message = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/p[1]").text
    ErrorMesList.append(str(i+1)+" "+message)

    i = i+1

# print(ErrorMesList)
for x in ErrorMesList:
 print (x)



# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('Arial', 'B', 10)
# for i in range(len(ErrorMesList)):
#
# # for x in ErrorMesList:
# #     print(x)
# #     # j= len(ErrorMesList)
# #     # while j < t:
#  pdf.cell(40, 10, ErrorMesList[i])
#  pdf.output('Error_message.pdf', 'F')







driver.quit()