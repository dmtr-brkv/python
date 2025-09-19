from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class mainPage:
    def __init__(self, browser):
        """
        Конструктор класса mainPage.

        :param browser: WebDriver — объект драйвера Selenium.
        """
        self.driver = browser

    def add_to_cart_sauce_labs_backpack(self):
        """
        Нажимает на кнопку Add to cart для товара Sauce Labs Backpack.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    def add_to_cart_sauce_labs_bike_light(self):
        """
        Нажимает на кнопку Add to cart для товара Sauce Labs Bike Light.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light").click()

    def add_to_cart_sauce_labs_bolt_t_shirt(self):
        """
        Нажимает на кнопку Add to cart для товара Sauce Labs Bolt T-Shirt.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    def shopping_cart_link(self):
        """
        Нажимает на кнопку Корзины.
        """
        basket_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        basket_button.click()