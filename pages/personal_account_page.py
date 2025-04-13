import allure
from selenium.common import TimeoutException
import locators
import config
from .base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = config.ACCOUNT_URL

    @allure.step("Открываем страницу личного кабинета")
    def open(self):
        super().open(self.url)

    @allure.step("Кликаем на ссылку 'История заказов'")
    def click_order_history_link(self):
        self.click(locators.ORDER_HISTORY_LINK)

    @allure.step("Кликаем на кнопку 'Выход'")
    def click_logout_button(self):
        self.click(locators.LOGOUT_BUTTON)

    @allure.step("Проверяем, что URL соответствует: {url}")
    def is_url_correct(self, url, timeout=10):
        return super().is_url_correct(url,timeout=10)

    @allure.step("Проверяем, что кнопка 'Выход' отображается")
    def is_logout_button_displayed(self):
        return self.is_element_visible(locators.LOGOUT_BUTTON)

    @allure.step("Получаем номер последнего заказа из истории заказов")
    def get_last_order_number(self):
        try:
            last_order_number_element = self.find_element(locators.LAST_ORDER_NUMBER_LOCATOR)
            return last_order_number_element.text
        except TimeoutException:
            return None

    @allure.step("Проверяем, что отображается ссылка 'История заказов'")
    def is_order_history_link_displayed(self):
        return self.is_element_visible(locators.ORDER_HISTORY_LINK)