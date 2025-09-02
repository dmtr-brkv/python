from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import re


edge_driver_path = r"C:\driver Edge\msedgedriver.exe"
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

fields = {
    "first-name": "Иван",
    "last-name": "Петров",
    "address": "Ленина, 55-3",
    "e-mail": "test@skypro.com",
    "phone": "+7985899998787",
    "city": "Москва",
    "country": "Россия",
    "job-position": "QA",
    "company": "SkyPro"
    }
for name_attr, value in fields.items():
    element = driver.find_element(By.CSS_SELECTOR, f"[name='{name_attr}']")
    element.send_keys(value)
    element.click()

submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary")
submit_button.click()

zip_code_element = driver.find_element(By.ID, "zip-code")
color_rgba = zip_code_element.value_of_css_property("background-color")

def rgba_to_hex(rgba_str):
    nums = re.findall(r'\d+', rgba_str)
    r, g, b = map(int, nums[:3])
    return f"#{r:02x}{g:02x}{b:02x}"

def test_zip_code():
    hex_color = rgba_to_hex(color_rgba)
    print(hex_color)
    assert hex_color == "#f8d7da"

    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city",
              "country", "job-position", "company"]
    for field_name in fields:
        field_element = driver.find_element(By.ID, field_name)
    rgba = field_element.value_of_css_property("background-color")
    color_hex = rgba_to_hex(rgba)
    print(field_name, color_hex)
    assert color_hex == "#d1e7dd"
    driver.quit()
