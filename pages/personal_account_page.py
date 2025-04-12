import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import config
import locators
from .Base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = config.ACCOUNT_URL

    @allure.step("Открываем страницу личного кабинета")
    def open(self):
        super().open(self.url)

    @allure.step("Кликаем на ссылку 'История заказов'")
    def click_order_history_link(self):
        super().click(locators.ORDER_HISTORY_LINK)

    @allure.step("Кликаем на кнопку 'Выход'")
    def click_logout_button(self):
        super().click(locators.LOGOUT_BUTTON)

    @allure.step("Проверяем, что URL соответствует: {url}")
    def is_url_correct(self, url, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    @allure.step("Проверяем, что кнопка 'Выход' отображается")
    def is_logout_button_displayed(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locators.LOGOUT_BUTTON)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Получаем номер последнего заказа из истории заказов")
    def get_last_order_number(self):
        try:
            last_order_number_element = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locators.LAST_ORDER_NUMBER_LOCATOR)
            )
            return last_order_number_element.text
        except TimeoutException:
            return None