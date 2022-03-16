import time
import smtplib
#from datetimedemo import utility
from fpdf import FPDF
from email.message import EmailMessage
#from PyPDF import PdfFileWriter, PdfFileReader

from PIL import Image

from selenium import webdriver
driver= webdriver.Chrome("C:/Users/QA/Pyhton_project/Pushp_Autotest\Chrome/chromedriver.exe")

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://casemgt.1wayit.com/")

#Locating Elements
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[1]/form/div[1]/input").send_keys("pushpender1wayit@gmail.com")
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[1]/form/div[2]/input").send_keys("12345678")
driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div[2]/div[1]/form/div[4]/input") .click()
#class PDF(FPDF):
#pdf= fpdf
#pdf= PDF()
#pdf= PDF(orientation='L')
#pdf.add_page()

for i in range(2,10):
    #driver.find_element_by_xpath("/html/body/app-root/div[2]/ul/li["+str(i)+"]/a").click()
    driver.find_element_by_xpath("/html/body/app-root/div[2]/ul/li["+str(i)+"]/a").click()
    time.sleep(5)
    #driver.save_screenshot("C:/Users/Devil/Desktop/Screenshot/image_"+utility.current_time()+".jpg")
    driver.save_screenshot("C:/Users/QA/Pyhton_project/Pushp_Autotest/Screenshot/image_"+str(i)+".jpg")
    pdf = FPDF()
    pdf.add_page(self,)

    #driver.save_screenshot("C:/Users/Devil/Desktop/Screenshot/image_"+str(i)+".jpg")
pdf.output("C:/Users/QA/Pyhton_project/Pushp_Autotest/PDF/PDFNew.pdf")

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