from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from calcPage import calcPage
import pytest

def test_res():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    calc_page = calcPage(browser)
    calc_page.text_input(45)
    calc_page.num_7()
    calc_page.sign_addition()
    calc_page.num_8()
    calc_page.sign_equally()
    to_be = calc_page.equally_15()
    assert to_be == "15"
    browser.quit()
