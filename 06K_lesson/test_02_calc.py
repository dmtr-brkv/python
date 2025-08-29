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
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

text_input = driver.find_element(By.CSS_SELECTOR, "#delay")
text_input.clear()
text_input.send_keys("45")

driver.find_element(By.XPATH, '//span[text()="7"]').click()
driver.find_element(By.XPATH, '//span[text()="+"]').click()
driver.find_element(By.XPATH, '//span[text()="8"]').click()
driver.find_element(By.XPATH, '//span[text()="="]').click()
element = WebDriverWait(driver, 50).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
)
res = driver.find_element(By.CSS_SELECTOR, ".screen").text
assert res == "15"

driver.quit()