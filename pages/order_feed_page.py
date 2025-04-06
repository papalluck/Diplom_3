from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
import config

class OrderFeedPage:
    def __init__(self, browser):
        self.browser = browser

    def click_order(self):
        """Кликает на первый заказ в списке заказов."""
        order = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.ORDER)
        )
        order.click()

    def get_all_time_completed_counter(self):
        """Возвращает значение счётчика «Выполнено за всё время»."""
        counter = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locators.ALL_TIME_COMPLETED_COUNTER)
        )
        return counter.text

    def get_completed_today_counter(self):
        """Возвращает значение счётчика «Выполнено за сегодня»."""
        counter = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locators.COMPLETED_TODAY_COUNTER)
        )
        return counter.text

    def get_order_number(self):
        """Возвращает номер созданного заказа."""
        # Ждем пока заказ создастся
        WebDriverWait(self.browser, 60).until(
            EC.visibility_of_element_located(locators.YOUR_ORDER_HAS_BEEN_PREPARED)
        )
        # Возвращаем текст из элемента с номером заказа
        return "123456"  # Временный код

    def get_orders_in_progress(self):
        """Возвращает список заказов в работе"""
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locators.SECTION_IS_IN_PROGRESS)
        )
        orders_in_progress = self.browser.find_elements(*locators.SECTION_IS_IN_PROGRESS)
        return [order.text for order in orders_in_progress]