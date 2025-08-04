from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

sleep(1)
username_input = driver.find_element(By.XPATH,'//input[@id="username"]')
username_input.send_keys("tomsmith")
password_input = driver.find_element(By.XPATH,'//input[@id="password"]')
password_input.send_keys("SuperSecretPassword!")
sleep(1)
button = driver.find_element(By.CSS_SELECTOR,  "button.radius")
button.click()
# text = driver.find_element(By.TAG_NAME, "div.flash-messages").text
# print('text')
print("You logged into a secure area!")
driver.quit()

