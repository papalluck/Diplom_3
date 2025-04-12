import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import locators
import config
from .Base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = config.LOGIN_URL

    @allure.step("Открываем страницу логина")
    def open(self):
        super().open(self.url)

    @allure.step("Вводим email")
    def enter_email(self, email):
        super().send_keys(locators.EMAIL_INPUT, email)

    @allure.step("Вводим пароль")
    def enter_password(self, password):
        super().send_keys(locators.PASSWORD_FIELD, password)

    @allure.step("Кликаем на кнопку 'Войти'")
    def click_login_button(self):
        super().click(locators.SIGN_IN_BUTTON)

    @allure.step("Логинимся в систему")
    def login(self, email, password):
        self.open()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Кликаем на кнопку 'Личный кабинет'")
    def click_personal_account_button(self):
        personal_account_button = WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable(locators.PERSONAL_ACCOUNT)
        )
        personal_account_button.click()


    @allure.step("Кликаем на кнопку 'Восстановить пароль'")
    def click_recover_password_button(self):
        super().click(locators.BUTTON_RECOVER_PASSWORD)

    @allure.step("Выходим из аккаунта")
    def logout(self):
        try:
            self.click_personal_account_button()
            super().click(locators.LOGOUT_BUTTON)
            super().is_url_correct(config.LOGIN_URL)
        except TimeoutException as e:
            print(f"Ошибка при выходе из аккаунта: {e}")
            raise