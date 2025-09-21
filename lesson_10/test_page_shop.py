from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from shop_main_page import mainPage
from shop_checkout_page import checkoutPage
from shop_authorization_page import autPage
from shop_step_one_page import stepOnePage

@allure.title("Тестирование магазина")
@allure.description("Тест проверяет корректность работу магазина "
                    "сравнивает стоимость добавленных товар с итоговой.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total():
    """
    Тест проверяет работу магазина, и сравнивает сумму добавленных в корзину товаров с ожидаемой.
    """
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    with allure.step("Открытие страницы авторизации"):
        AutPage = autPage(browser)
    with allure.step("Ввод имени пользователя"):
        AutPage.user_name()
    with allure.step("Ввод пароля пользователя"):
        AutPage.password()
    with allure.step("Нажимает на кнопку Login"):
        AutPage.login_button()

    with allure.step("Открытие главной страницы магазина"):
        MainPage = mainPage(browser)
    with allure.step("Добавление товара Sauce Labs Backpack в корзину"):
        MainPage.add_to_cart_sauce_labs_backpack()
    with allure.step("Добавление товара Sauce Labs Bike Light в корзину"):
        MainPage.add_to_cart_sauce_labs_bike_light()
    with allure.step("Добавление товара Sauce Labs Bolt T-Shirt в корзину"):
        MainPage.add_to_cart_sauce_labs_bolt_t_shirt()
    with allure.step("Переходит в Корзину"):
        MainPage.shopping_cart_link()

    with allure.step("Переходит на страницу проверки"):
        CheckoutPage = checkoutPage(browser)
    with allure.step("Переходит на страницу проверки"):
        CheckoutPage.checkount()

    with allure.step("Переходит на страницу заполнения информации"):
        StepOne = stepOnePage(browser)
    with allure.step("Ввод имени пользователя"):
        StepOne.first_name()
    with allure.step("Ввод фамилию пользователя"):
        StepOne.last_name()
    with allure.step("Вводит почтовый индекс пользователя"):
        StepOne.postalCode()
    with allure.step("Переходит на страницу итогов"):
        StepOne.button()

    with allure.step("Сохранение результата"):
        total = StepOne.total()
    with allure.step("Проверка результата с ожидаемым"):
        assert total == 'Total: $58.29'

    browser.quit()
