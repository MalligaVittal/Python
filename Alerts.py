from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name= "Malliga"                 # since we can change the names we are storing it in name variable
driver.find_element(By.NAME, "enter-name").send_keys(name)          # calling the name variable here
driver.find_element(By.ID, "alertbtn").click()
alerts = driver.switch_to.alert                # switching from webdriver to alerts then only we can click alert
alertText= alerts.text                         #  retrieving the text of the popup here
print(alertText)
sleep(5)
alerts.accept()                  # accept the popup
# alerts.dismiss()               # Reject the popup
