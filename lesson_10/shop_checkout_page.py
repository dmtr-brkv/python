from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class checkoutPage:
    def __init__(self, browser):
        """
        Конструктор класса checkoutPage.

        :param browser: WebDriver — объект драйвера Selenium.
        """
        self.driver = browser

    def checkount(self):
        """
        Нажимает на кнопку Сheckount.
        """
        checkount = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'checkout')))
        checkount.click()