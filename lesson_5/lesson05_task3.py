from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")


search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("Sky", Keys.RETURN)
sleep(1)
search_input.clear()
sleep(1)
search_input.send_keys("Pro", Keys.RETURN)
sleep(3)
driver.quit()