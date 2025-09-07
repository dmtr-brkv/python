from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class calcPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.wait = WebDriverWait(driver, 10)

    def text_input(self, time):
        text_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        text_input.clear()
        text_input.send_keys(time)

    def num_1(self):
        self.driver.find_element(By.XPATH, '//span[text()="1"]').click()
    def num_2(self):
        self.driver.find_element(By.XPATH, '//span[text()="2"]').click()
    def num_3(self):
        self.driver.find_element(By.XPATH, '//span[text()="3"]').click()
    def num_4(self):
        self.driver.find_element(By.XPATH, '//span[text()="4"]').click()
    def num_5(self):
        self.driver.find_element(By.XPATH, '//span[text()="5"]').click()
    def num_6(self):
        self.driver.find_element(By.XPATH, '//span[text()="6"]').click()
    def num_7(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
    def num_8(self):
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
    def num_9(self):
        self.driver.find_element(By.XPATH, '//span[text()="9"]').click()
    def num_0(self):
        self.driver.find_element(By.XPATH, '//span[text()="0"]').click()
    def sign_addition(self):
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
    def sign_division(self):
        self.driver.find_element(By.XPATH, '//span[text()="÷"]').click()
    def sign_multiplication(self):
        self.driver.find_element(By.XPATH, '//span[text()="x"]').click()
    def sign_deduction(self):
        self.driver.find_element(By.XPATH, '//span[text()="-"]').click()
    def sign_equally(self):
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()
    def sign_point(self):
        self.driver.find_element(By.XPATH, '//span[text()="."]').click()

    def equally_15(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        res = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return res


