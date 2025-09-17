from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class mainPage:
    def __init__(self, browser):
        self.driver = browser

    @allure.step("Нажимает на кнопку Add to cart для товара Sauce Labs Backpack")
    def add_to_cart_sauce_labs_backpack(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    @allure.step("Нажимает на кнопку Add to cart для товара Sauce Labs Bike Light")
    def add_to_cart_sauce_labs_bike_light(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light").click()

    @allure.step("Нажимает на кнопку Add to cart для товара Sauce Labs Bolt T-Shirt")
    def add_to_cart_sauce_labs_bolt_t_shirt(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    @allure.step("Нажимает на кнопку Корзины")
    def shopping_cart_link(self):
        basket_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        basket_button.click()