import allure
from selenium.common.exceptions import TimeoutException
import locators
import config
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = config.LOGIN_URL

    @allure.step("Открываем страницу логина")
    def open(self):
        super().open(self.url)

    @allure.step("Вводим email")
    def enter_email(self, email):
        self.send_keys(locators.EMAIL_INPUT, email)

    @allure.step("Вводим пароль")
    def enter_password(self, password):
        self.send_keys(locators.PASSWORD_FIELD, password)

    @allure.step("Кликаем на кнопку 'Войти'")
    def click_login_button(self):
        self.click(locators.SIGN_IN_BUTTON)

    @allure.step("Проверяем, что мы на странице забытого пароля")
    def is_forgot_password_page(self):
        return self.is_url_correct(config.FORGOT_PASSWORD_URL)

    @allure.step("Логинимся в систему")
    def login(self, email, password):
        self.open()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Кликаем на кнопку 'Личный кабинет'")
    def click_personal_account_button(self):
        self.click(locators.PERSONAL_ACCOUNT)

    @allure.step("Кликаем на кнопку 'Восстановить пароль'")
    def click_recover_password_button(self):
        self.click(locators.BUTTON_RECOVER_PASSWORD)

    @allure.step("Выходим из аккаунта")
    def logout(self):
        try:
            self.click_personal_account_button()
            self.click(locators.LOGOUT_BUTTON)
            self.is_url_correct(config.LOGIN_URL)
        except TimeoutException as e:
            raise e