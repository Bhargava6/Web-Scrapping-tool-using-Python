from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from twilio.rest import Client
from webdriver_manager.chrome import ChromeDriverManager


URL = 'https://erp.mlrinstitutions.ac.in/Login.aspx?ReturnUrl=%2f

chrome_driver = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=chrome_driver, options=webdriver.ChromeOptions()) driver.get(URL)
user_name = driver.find_element(By.XPATH, '//*[@id="txtUserName"]') user_name.send_keys("*********")#Replace stars with your Username
next = driver.find_element(By.XPATH. '//*[@id="btnNext"]')
next.click()
time.sleep(5)
password = driver.find_element(By.XPATH, '//*[@id="txtPassword"]") password.send_keys("*********") #Replace stars with your Password
submit = driver.find_element(By.XPATH. '//*[@id="btnSubmit"]')
submit.click()
time.sleep(5)

attendence= driver.find_element(By.XPATH, //*[@id="ctl00_cpStud_lblTotalPercentage
account_sid =#your twilio account sid
auth_token= #your Auth token id
client= Client(account sid, auth_token)
message= client.messages.create (body= f" Your present Attendence is( My_attendence)", from_="+ 14346089632", to='+917788994455*
2112 #Replace the above phone number with your number  
