from selenium.webdriver import ActionChains
import config
import locators
import allure
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from pages.Base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = config.BASE_URL

    @allure.step("Открываем главную страницу")
    def open(self):
        super().open(self.url)

    @allure.step("Кликаем на ссылку 'Конструктор'")
    def click_constructor_link(self):
        super().click(locators.CONSTRUCTOR_LINK)

    @allure.step("Кликаем на ссылку 'Лента заказов'")
    def click_order_feed_link(self):
        super().click(locators.ORDER_FEED_LINK)

    @allure.step("Кликаем на ингредиент")
    def click_ingredient(self):
        super().click(locators.FLUORESCENT_BUN)

    @allure.step("Кликаем на кнопку 'Закрыть'")
    def click_close_button(self):
        super().click(locators.CLOSE_BUTTON)

    @allure.step("Получаем значение счетчика ингредиентов")
    def get_ingredient_counter(self):
        try:
            counter = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locators.INGREDIENT_COUNTER)
            )
            return counter.text
        except TimeoutException:
            return None

    @allure.step("Перетаскиваем ингредиент")
    def drag_and_drop_ingredient(self, ingredient_locator):
        try:
            source = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(ingredient_locator)
            )
            target = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(locators.BURGER_CONSTRUCTOR_BASKET)
            )

            action_chains = ActionChains(self.browser)
            action_chains.drag_and_drop(source, target).perform()
        except TimeoutException as e:
             raise TimeoutException(f"Не удалось перетащить ингредиент за {e}")

    @allure.step("Кликаем на кнопку 'Оформить заказ'")
    def click_checkout_button(self):
        super().click(locators.CHECKOUT_BUTTON)

    @allure.step("Создаем новый заказ")
    def create_new_order(self):
        self.drag_and_drop_ingredient(locators.FLUORESCENT_BUN)
        self.drag_and_drop_ingredient(locators.SAUCE_SPICY_X)
        self.click_checkout_button()

        WebDriverWait(self.browser, 30).until(
            EC.text_to_be_present_in_element(locators.CREATED_ORDER_NUMBER, "9999"))

        WebDriverWait(self.browser, 30).until(
            lambda driver: driver.find_element(*locators.CREATED_ORDER_NUMBER).text != "9999"
        )

        return self.get_order_number()

    @allure.step("Получаем номер созданного заказа")
    def get_order_number(self):
        order_number_element = self.browser.find_element(*locators.CREATED_ORDER_NUMBER)
        return order_number_element.text

    @allure.step("Закрываем всплывающее окно о создании заказа")
    def close_new_order(self):
        try:
            close_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(locators.CLOSE_BUTTON_NEW_ORDER)
            )
            self.browser.execute_script("arguments[0].click();", close_button)
        except TimeoutException:
            raise TimeoutException("Не дождались кликабельности кнопки закрытия попапа")
        except ElementClickInterceptedException:
            raise ElementClickInterceptedException("Кнопка закрытия перекрыта другим элементом")
