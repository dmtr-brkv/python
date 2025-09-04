from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from shop_main_page import mainPage
from shop_checkout_page import checkoutPage
from shop_authorization_page import autPage
from shop_step_one_page import stepOnePage

def test_shop_total():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    AutPage = autPage(browser)
    AutPage.user_name()
    AutPage.password()
    AutPage.login_button()

    MainPage = mainPage(browser)
    MainPage.add_to_cart_sauce_labs_backpack()
    MainPage.add_to_cart_sauce_labs_bike_light()
    MainPage.add_to_cart_sauce_labs_bolt_t_shirt()
    MainPage.shopping_cart_link()

    CheckoutPage = checkoutPage(browser)
    CheckoutPage.checkount()

    StepOne = stepOnePage(browser)
    StepOne.first_name()
    StepOne.last_name()
    StepOne.postalCode()
    StepOne.button()

    total = StepOne.total()
    assert total == 'Total: $58.29'

    browser.quit()
