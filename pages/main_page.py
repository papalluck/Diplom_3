import re
from selenium.webdriver import ActionChains
import config
import locators
import allure
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = config.BASE_URL

    @allure.step("Открываем главную страницу")
    def open(self):
        super().open(self.url)

    @allure.step("Кликаем на ссылку 'Конструктор'")
    def click_constructor_link(self):
        self.click(locators.CONSTRUCTOR_LINK)

    @allure.step("Кликаем на ссылку 'Лента заказов'")
    def click_order_feed_link(self):
        self.click(locators.ORDER_FEED_LINK)

    @allure.step("Кликаем на ингредиент")
    def click_ingredient(self):
        self.click(locators.FLUORESCENT_BUN)

    @allure.step("Кликаем на кнопку 'Закрыть'")
    def click_close_button(self):
        self.click(locators.CLOSE_BUTTON)

    @allure.step("Получаем значение счетчика ингредиентов")
    def get_ingredient_counter(self):
        try:
            counter = self.find_element(locators.INGREDIENT_COUNTER)
            return counter.text
        except TimeoutException:
            return None

    @allure.step("Перетаскиваем булку")
    def drag_and_drop_bun(self):
        self.drag_and_drop_ingredient(locators.FLUORESCENT_BUN)

    @allure.step("Перетаскиваем соус")
    def drag_and_drop_sauce(self):
        self.drag_and_drop_ingredient(locators.SAUCE_SPICY_X)

    @allure.step("Перетаскиваем ингредиент")
    def drag_and_drop_ingredient(self, ingredient_locator):
        try:
            source = self.find_element(ingredient_locator)
            target = self.find_element(locators.BURGER_CONSTRUCTOR_BASKET)

            action_chains = ActionChains(self.browser)
            action_chains.drag_and_drop(source, target).perform()
        except TimeoutException as e:
            raise TimeoutException(f"Не удалось перетащить ингредиент за {e}")

    @allure.step("Кликаем на кнопку 'Оформить заказ'")
    def click_checkout_button(self):
        self.click(locators.CHECKOUT_BUTTON)

    @allure.step("Ожидаем загрузку номера заказа")
    def wait_for_order_number_to_load(self, timeout=30):
        self.wait_for_text_to_match_regex(locators.CREATED_ORDER_NUMBER, r"^\d{6}$", timeout)

    @allure.step("Создаем новый заказ и дожидаемся загрузки номера заказа")
    def create_new_order(self):
        self.drag_and_drop_bun()
        self.drag_and_drop_sauce()
        self.click_checkout_button()
        self.wait_for_order_number_to_load()
        order_number = self.get_order_number()
        self.close_new_order()
        return order_number

    @allure.step("Ожидаем, пока номер заказа изменится")
    def wait_for_order_number_to_be_different_from_default(self, timeout=30):
        self.wait_for_text_to_be_different(locators.CREATED_ORDER_NUMBER, "9999", timeout)

    @allure.step("Получаем номер созданного заказа")
    def get_order_number(self):
        order_number_element = self.find_element(locators.CREATED_ORDER_NUMBER)
        return order_number_element.text

    @allure.step("Закрываем всплывающее окно о создании заказа")
    def close_new_order(self):
        try:
            close_button = self.find_element(locators.CLOSE_BUTTON_NEW_ORDER)
            self.browser.execute_script("arguments[0].click();", close_button)
        except TimeoutException:
            raise TimeoutException("Не дождались кликабельности кнопки закрытия попапа")
        except ElementClickInterceptedException:
            raise ElementClickInterceptedException("Кнопка закрытия попапа перекрыта другим элементом")

    @allure.step("Кликаем на кнопку 'Личный кабинет'")
    def click_personal_account_button(self):
        self.wait_for_personal_account_button_visibility()
        self.click(locators.PERSONAL_ACCOUNT)

    @allure.step("Ожидаем, пока кнопка 'Личный кабинет' станет видимой")
    def wait_for_personal_account_button_visibility(self, timeout=10):
        self.is_element_visible(locators.PERSONAL_ACCOUNT, timeout)

    @allure.step("Проверяем, что ссылка 'Конструктор' активна")
    def is_constructor_link_active(self):
        return self.element_to_be_clickable(locators.ACTIVE_CONSTRUCTOR_LINK)

    @allure.step("Проверяем, что отображается сообщение об успешном оформлении заказа")
    def is_checkout_successful(self):
        return self.is_element_visible(locators.YOUR_ORDER_HAS_BEEN_PREPARED)

    @allure.step("Проверяем, что отображается всплывающее окно ингредиента")
    def is_ingredient_popup_visible(self):
        return self.is_element_visible(locators.INGREDIENT_DETAILS)

    @allure.step("Проверяем, что не отображается всплывающее окно ингредиента")
    def is_ingredient_popup_invisible(self):
        return self.is_element_invisible(locators.INGREDIENT_DETAILS)