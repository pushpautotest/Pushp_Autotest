import time
#from PIL import Image
import smtplib
#from datetimedemo import utility
from email.message import EmailMessage

from selenium import webdriver
driver= webdriver.Chrome("C:/Users/Devil/PycharmProjects/Pushp_Autotest/Chrome/chromedriver.exe")

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://casemgt.1wayit.com/#/login")

#Locating Elements
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[1]/form/div[1]/input").send_keys("pushpender1wayit@gmail.com")
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[1]/form/div[2]/input").send_keys("12345678")
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[1]/form/div[4]/input") .click()
pdf= FPDF()
pdf.add_page()
pdf.set_font("Arial", size=20)
for i in range(2,10):
    #driver.find_element_by_xpath("/html/body/app-root/div[2]/ul/li["+str(i)+"]/a").click()
    driver.find_element_by_xpath("/html/body/app-root/div[2]/ul/li["+str(i)+"]/a").click()
    time.sleep(5)
    #driver.save_screenshot("C:/Users/Devil/Desktop/Screenshot/image_"+utility.current_time()+".jpg")
    driver.save_screenshot("C:/Users/Devil/Desktop/Screenshot/image_"+str(i)+".jpg")

pdf.output("C:/Users/Devil/PycharmProjects/Pushp_Autotest/PDFNew.pdf")

#email Triggering
sender_email="pushpender1wayit@gmail.com"
Password="pushpender007"
receiver_email="pushp.bardhan@gmail.com"

server= smtplib.SMTP_SSL('smtp.gmail.com',465)
msg=EmailMessage()
server.login(sender_email, Password)

msg['From']=sender_email
msg['Subject']='Test Subject'
msg['To']=receiver_email
msg.set_content("This is a test email to check the functionality\n\n Many Thanks\nPushpender")
server.send_message(msg)
server.quit()
driver.quit()