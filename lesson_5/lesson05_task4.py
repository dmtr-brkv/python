from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

sleep(1)
username_input = driver.find_element(By.XPATH, '//input[@id="username"]')
username_input.send_keys("tomsmith")
password_input = driver.find_element(By.XPATH, '//input[@id="password"]')
password_input.send_keys("SuperSecretPassword!")
sleep(1)
button = driver.find_element(By.CSS_SELECTOR,  "button.radius")
button.click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located
                     ((By.ID, "flash-messages")))
print(element.text)

driver.quit()
