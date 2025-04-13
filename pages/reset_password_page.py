import locators
import config
import allure
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage



class ResetPasswordPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = config.RESET_PASSWORD_URL

    @allure.step("Открываем страницу сброса пароля")
    def open(self):
        super().open(self.url)

    @allure.step("Вводим email для сброса пароля")
    def enter_email(self, email):
        self.send_keys(locators.EMAIL_INPUT, email)

    @allure.step("Кликаем на кнопку 'Восстановить'")
    def click_restore_button(self):
        self.click(locators.RESTORE_BUTTON)

    @allure.step("Вводим новый пароль")
    def enter_password(self, password):
        self.send_keys(locators.PASSWORD_INPUT, password)

    @allure.step("Кликаем на кнопку 'Сохранить'")
    def click_save_button(self):
        self.click(locators.SAVE_BUTTON)

    @allure.step("Кликаем на кнопку 'Показать/Скрыть пароль'")
    def click_show_hide_password_button(self):
        self.click(locators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step("Проверяем, что поле пароля активно")
    def is_password_field_active(self):
        try:
            self.element_to_be_clickable(locators.ACTIVE_PASSWORD_FIELD)
            return True
        except TimeoutException:
            return False

    @allure.step("Проверяем, что мы на странице сброса пароля")
    def is_reset_password_page(self):
        return self.is_url_correct(config.RESET_PASSWORD_URL)

    @allure.step("Проверяем, что кнопка 'Сохранить' отображается")
    def is_save_button_displayed(self):
        try:
            self.element_to_be_clickable(locators.SAVE_BUTTON)
            return True
        except TimeoutException:
            return False