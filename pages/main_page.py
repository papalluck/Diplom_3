from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import locators
import time

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = config.BASE_URL

    def open(self):
        self.browser.get(self.url)

    def click_constructor_link(self):
        constructor_link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.CONSTRUCTOR_LINK)
        )
        constructor_link.click()

    def click_order_feed_link(self):
        order_feed_link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.ORDER_FEED_LINK)
        )
        order_feed_link.click()

    def click_ingredient(self):
        ingredient = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.FLUORESCENT_BUN)
        )
        ingredient.click()

    def click_close_button(self):
        close_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.CLOSE_BUTTON)
        )
        close_button.click()

    def get_ingredient_counter(self):
        try:
            counter = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locators.INGREDIENT_COUNTER)
            )
            return counter.text
        except:
            return None

    def drag_and_drop_ingredient(self, ingredient_locator):
        """Перетаскивает ингредиент в область заказа."""
        source = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ingredient_locator)
        )
        target = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locators.BURGER_CONSTRUCTOR_BASKET)
        )

        action_chains = ActionChains(self.browser)
        action_chains.drag_and_drop(source, target).perform()

    def click_checkout_button(self):
        checkout_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.CHECKOUT_BUTTON)
        )
        checkout_button.click()

    def create_new_order(self):
        """Создает новый заказ."""
        self.drag_and_drop_ingredient(locators.FLUORESCENT_BUN)
        self.drag_and_drop_ingredient(locators.SAUCE_SPICY_X)

        checkout_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.CHECKOUT_BUTTON)
        )
        checkout_button.click()

    def get_order_number(self):
        """Получает номер созданного заказа."""
        order_number_element = self.browser.find_element(*locators.CREATED_ORDER_NUMBER)
        return order_number_element.text

    def close_new_order_popup(self):
        """Закрывает всплывающее окно о создании заказа."""
        close_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.CLOSE_BUTTON_NEW_ORDER)
        )
        self.browser.execute_script("arguments[0].click();", close_button)