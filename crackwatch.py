import time
import smtplib
import keyring
import getpass
import chromedriver_binary  # Adds chromedriver binary to path
from pprint import pprint
from selenium import webdriver
from email.message import EmailMessage
from selenium.webdriver.chrome.options import Options

#Driver
url = "https://crackwatch.com/game/assassin-s-creed-valhalla"

#chrome Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

#go to page 
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(10)
#click initial pop up
driver.find_element_by_xpath('//*[@id="react-root"]/div/div[1]/div/div/div[5]').click()
time.sleep(2)

#gmail server
server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587

#specify sender and receiver for email
senderEmail = input('Please enter your email: ')
senderPassword = getpass.getpass('Please enter your password: ')
receiver = input('Please enter the email you wish to send the notification to: ')

#use keyring to securely store sender email and password
keyring.set_password("email", senderEmail, senderPassword)

#cracked and uncracked messages
uncrackedMsg = 'GAME NOT CRACKED YET'
crackedMsg = 'GAME CRACKED'

#function to login to gmail server and specify sender and receiver
def sendEmail(message):
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(senderEmail, keyring.get_password("email", senderEmail))
    server.sendmail(senderEmail, receiver, message)
    server.close() 

#'''get status
# if status is uncracked send email saying uncracked
# else send email saying cracked'''
status = driver.find_element_by_class_name('status-bottom')
if status.text == 'UNCRACKED':
    sendEmail(uncrackedMsg) 
else:
    sendEmail(crackedMsg)        

#close browser
driver.close()