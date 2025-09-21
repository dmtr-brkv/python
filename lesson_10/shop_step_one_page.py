from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class stepOnePage:
    def __init__(self, browser):
        """
        Конструктор класса stepOnePage.

        :param browser: WebDriver — объект драйвера Selenium.
        """
        self.driver = browser

    def first_name(self):
        """
        Вводит имя пользователя.
        """
        first_name = self.driver.find_element(By.CSS_SELECTOR, "[name='firstName']")
        first_name.send_keys("Дмирий")

    def last_name(self):
        """
        Вводит фамилию пользователя.
        """
        last_name = self.driver.find_element(By.CSS_SELECTOR, "[name='lastName']")
        last_name.send_keys("Бирюков")

    def postalCode(self):
        """
        Вводит почтовый индекс пользователя.
        """
        postalCode = self.driver.find_element(By.CSS_SELECTOR, "[name='postalCode']")
        postalCode.send_keys("606400")

    def button(self):
        """
        Нажимает кнопку Continue.
        """
        button = self.driver.find_element(By.ID, "continue")
        button.click()

    def total(self):
        """
        Получение результата покупки.
        """
        total = self.driver.find_element(By.CSS_SELECTOR, "[data-test='total-label").text
        return total