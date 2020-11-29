from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary  # Adds chromedriver binary to path
from pprint import pprint
import time
import smtplib
from email.message import EmailMessage

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
sender = 'devoneloper718@gmail.com'
receiver = 'rhrimon@gmail.com'

#cracked and uncracked messages
uncrackedMsg = 'GAME NOT CRACKED YET'
crackedMsg = 'GAME CRACKED'

def sendEmail(message):
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('devoneloper718@gmail.com','devpassword')
    server.sendmail('devoneloper718@gmail.com','rhrimon@gmail.com', message)
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