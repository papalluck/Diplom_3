import locators
import allure
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderFeedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Кликаем на первый заказ в списке заказов")
    def click_order(self):
        self.click(locators.ORDER)

    @allure.step("Получаем значение счётчика «Выполнено за всё время»")
    def get_all_time_completed_counter(self):
        try:
            element = self.find_element(locators.ALL_TIME_COMPLETED_COUNTER)
            return element.text
        except TimeoutException:
            return None

    @allure.step("Получаем значение счётчика «Выполнено за сегодня»")
    def get_completed_today_counter(self):
        try:
            element = self.find_element(locators.COMPLETED_TODAY_COUNTER)
            return element.text
        except TimeoutException:
            return None

    @allure.step("Получаем номер созданного заказа")
    def get_order_number(self):
        try:
            self.element_to_be_clickable(locators.YOUR_ORDER_HAS_BEEN_PREPARED)
            order_number_element = self.find_element(locators.CREATED_ORDER_NUMBER)
            return order_number_element.text
        except TimeoutException as e:
            raise TimeoutException(f"Не удалось получить номер заказа {e}")

    @allure.step("Получаем список заказов в работе")
    def get_orders_in_progress(self, locator):
        try:
            self.wait_for_element_visibility(locator)
            orders_in_progress = self.find_elements(locator)
            return [order.text for order in orders_in_progress]
        except TimeoutException as e:
            raise TimeoutException(f"Не удалось получить список заказов в работе {e}")

    @allure.step("Проверяем, что отображаются детали заказа")
    def is_order_details_displayed(self):
        return self.is_element_visible(locators.ORDER_DETAILS_POP_UP)

    @allure.step("Проверяем, что отображается счетчик 'Выполнено за всё время'")
    def is_all_time_completed_counter_displayed(self):
        return self.is_element_visible(locators.ALL_TIME_COMPLETED_COUNTER)

    @allure.step("Проверяем, что отображается счетчик 'Выполнено за сегодня'")
    def is_completed_today_counter_displayed(self):
        return self.is_element_visible(locators.COMPLETED_TODAY_COUNTER)

    @allure.step("Проверяем, что заказ с номером {order_number} находится в списке 'В работе'")
    def is_order_present_in_progress(self, locator, order_number):
        orders_in_progress = self.get_orders_in_progress(locator)
        return any(order_number in order for order in orders_in_progress)

    @allure.step("Ожидаем, пока заказ с номером {order_number} появится в списке 'В работе'")
    def wait_for_order_to_be_in_progress(self, order_number):
        self.wait_for_order_in_progress(locators.SECTION_IS_IN_PROGRESS, order_number)

    @allure.step("Проверяем, что заказ с номером {order_number} отображается в списке 'В работе'")
    def is_order_in_progress_displayed(self, order_number):
        return self.is_order_present_in_progress(locators.SECTION_IS_IN_PROGRESS, order_number)