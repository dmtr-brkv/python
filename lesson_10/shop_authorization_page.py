from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class autPage:
    def __init__(self, driver):
        """
        Конструктор класса autPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 10)

    def user_name(self):
        """
        Вводит имя пользователя.
        """
        user_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='user-name']")))
        user_name.send_keys("standard_user")

    def password(self):
        """
        Вводит пароль пользователя.
        """
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='password']")))
        password.send_keys("secret_sauce")

    def login_button(self):
        """
        Нажимает на кнопку Login.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()