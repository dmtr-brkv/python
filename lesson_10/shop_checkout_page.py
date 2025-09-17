from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class checkoutPage:
    def __init__(self, browser):
        self.driver = browser

    @allure.step("Нажимает на кнопку Сheckount")
    def checkount(self):
        checkount = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'checkout')))
        checkount.click()