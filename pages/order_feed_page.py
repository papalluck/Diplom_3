from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
import allure
from selenium.common.exceptions import TimeoutException
from pages.Base_page import BasePage

class OrderFeedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Кликаем на первый заказ в списке заказов")
    def click_order(self):
        super().click(locators.ORDER)

    @allure.step("Получаем значение счётчика «Выполнено за всё время»")
    def get_all_time_completed_counter(self):
        try:
             element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locators.ALL_TIME_COMPLETED_COUNTER))
             return element.text
        except TimeoutException:
          return None


    @allure.step("Получаем значение счётчика «Выполнено за сегодня»")
    def get_completed_today_counter(self):
        try:
             element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locators.COMPLETED_TODAY_COUNTER))
             return element.text
        except TimeoutException:
          return None
    @allure.step("Получаем номер созданного заказа")
    def get_order_number(self):
        try:
            WebDriverWait(self.browser, 60).until(
                EC.visibility_of_element_located(locators.YOUR_ORDER_HAS_BEEN_PREPARED)
            )
            order_number_element = self.browser.find_element(*locators.CREATED_ORDER_NUMBER)
            return order_number_element.text
        except TimeoutException as e:
             raise TimeoutException(f"Не удалось получить номер заказа {e}")


    @allure.step("Получаем список заказов в работе")
    def get_orders_in_progress(self):
        try:
             WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locators.SECTION_IS_IN_PROGRESS))
             orders_in_progress = self.browser.find_elements(*locators.SECTION_IS_IN_PROGRESS)
             return [order.text for order in orders_in_progress]
        except TimeoutException as e:
             raise TimeoutException(f"Не удалось получить список заказов в работе {e}")