from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class autPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 10)

    def user_name(self):
        user_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='user-name']")))
        user_name.send_keys("standard_user")

    def password(self):
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='password']")))
        password.send_keys("secret_sauce")

    def login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()