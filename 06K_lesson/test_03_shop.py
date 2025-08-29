from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)
user_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[name='user-name']")))
user_name.send_keys("standard_user")
# user_name.click()

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[name='password']")))
password.send_keys("secret_sauce")
# password.click()

driver.find_element(By.CSS_SELECTOR, "#login-button").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
basket_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
)
basket_button.click()
Checkount = WebDriverWait (driver,10).until(
    EC.element_to_be_clickable((By.ID,'checkout'))
)
Checkount.click()

first_name = driver.find_element(By.CSS_SELECTOR, "[name='firstName']")
first_name.send_keys("Дмирий")

last_name = driver.find_element(By.CSS_SELECTOR, "[name='lastName']")
last_name.send_keys("Бирюков")

postalCode = driver.find_element(By.CSS_SELECTOR, "[name='postalCode']")
postalCode.send_keys("606400")

button = driver.find_element(By.ID, "continue")
button.click()

Total = driver.find_element(By.CSS_SELECTOR, "[data-test='total-label").text
print(Total)
driver.quit()

assert Total == 'Total: $58.29'
