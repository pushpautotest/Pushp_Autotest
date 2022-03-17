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

driver.get("https://www.mylagro.com/")
driver.find_element_by_xpath("/html/body/div[10]/div/div/div/div[2]/ul/li[2]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//div/nav/div/ul[2]/li[3]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[1]/div/i[2]").click()
time.sleep(5)

ErrorMesList=[]
a = "@yopmail.com"
lenth = 10
i=0
while i < 2:
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[1]/div/input").send_keys("ragav@yopmail.com")
    psw1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k = lenth))
    e = str(psw1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[2]/div/input").send_keys(e)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[4]/button").click()
    time.sleep(10)
    message = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/p[1]").text
    ErrorMesList.append(message)
    print (str(i+1)+' '+ message)
    i = i+1


# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('Arial', 'I', 10)
# pdf.cell(40, 10, message)
# pdf.output('tuto1.pdf', 'F')
