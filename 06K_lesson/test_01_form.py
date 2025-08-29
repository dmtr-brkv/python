from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

edge_driver_path = r"C:\driver Edge\msedgedriver.exe"
service = Service(edge_driver_path)
driver = webdriver.Edge(service=EdgeService(edge_driver_path))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
first_name.send_keys("Иван")
first_name.click()


last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
last_name.send_keys("Петров")
last_name.click()


address_input = driver.find_element(By.CSS_SELECTOR, "[name='address']")
address_input.send_keys("Ленина, 55-3")
address_input.click()


email_address = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
email_address.send_keys("test@skypro.com")
email_address.click()


phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
phone_number.send_keys("+7985899998787")
phone_number.click()


city_name = driver.find_element(By.CSS_SELECTOR, "[name='city']")
city_name.send_keys("Москва")
city_name.click()


country_name = driver.find_element(By.CSS_SELECTOR, "[name='country']")
country_name.send_keys("Россия")
country_name.click()


job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
job_position.send_keys("QA")
job_position.click()


company_name = driver.find_element(By.CSS_SELECTOR, "[name='company']")
company_name.send_keys("SkyPro")
company_name.click()

submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary")
submit_button.click()

zip_code_element = driver.find_element(By.ID, "zip-code")
color_rgba = zip_code_element.value_of_css_property("background-color")
import re

def rgba_to_hex(rgba_str):
    nums = re.findall(r'\d+', rgba_str)
    r, g, b = map(int, nums[:3])
    return f"#{r:02x}{g:02x}{b:02x}"

hex_color = rgba_to_hex(color_rgba)
print(hex_color)

assert hex_color == "#f8d7da"

fields = ["first-name", "last-name", "address", "email", "phone", "city", "country", "job", "company"]
for field in fields:
    field = driver.find_element(By.ID, "first-name")
rgba = field.value_of_css_property("background-color")

def rgba_to_hex(rgba_str):
    import re
    nums = re.findall(r'\d+', rgba_str)
    r, g, b = map(int, nums[:3])
    return f"#{r:02x}{g:02x}{b:02x}"

color_hex = rgba_to_hex(rgba)

assert color_hex == "#d1e7dd"

driver.quit()
