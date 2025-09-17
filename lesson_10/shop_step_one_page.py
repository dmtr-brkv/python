from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class stepOnePage:
    def __init__(self, browser):
        self.driver = browser

    @allure.step("Вводит имя пользователя")
    def first_name(self):
        first_name = self.driver.find_element(By.CSS_SELECTOR, "[name='firstName']")
        first_name.send_keys("Дмирий")

    @allure.step("Вводит фамилию пользователя")
    def last_name(self):
        last_name = self.driver.find_element(By.CSS_SELECTOR, "[name='lastName']")
        last_name.send_keys("Бирюков")

    @allure.step("Вводит почтовый индекс пользователя")
    def postalCode(self):
        postalCode = self.driver.find_element(By.CSS_SELECTOR, "[name='postalCode']")
        postalCode.send_keys("606400")

    @allure.step("Нажимает кнопку Continue")
    def button(self):
        button = self.driver.find_element(By.ID, "continue")
        button.click()

    @allure.step("Получение результата покупки")
    def total(self):
        total = self.driver.find_element(By.CSS_SELECTOR, "[data-test='total-label").text
        return total