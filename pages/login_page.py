from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
import config

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = config.LOGIN_URL

    def open(self):
        self.browser.get(self.url)

    def enter_email(self, email):
        email_field = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.EMAIL_INPUT)
        )
        email_field.click()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.PASSWORD_FIELD)
        )
        password_field.click()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.SIGN_IN_BUTTON)
        )
        login_button.click()

    def login(self, email, password):
        self.open()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def click_personal_account_button(self):
        personal_account_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.PERSONAL_ACCOUNT)
        )
        personal_account_button.click()

    def click_recover_password_button(self):
        recover_password_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.BUTTON_RECOVER_PASSWORD)
        )
        recover_password_button.click()

    def logout(self):
        try:
            self.click_personal_account_button()
            logout_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(locators.LOGOUT_BUTTON)
            )
            self.browser.execute_script("arguments[0].click();", logout_button)
            WebDriverWait(self.browser, 10).until(EC.url_to_be(config.LOGIN_URL))
        except Exception as e:
            print(f"Ошибка при выходе из аккаунта: {e}")
            raise  # Перебросить исключение, чтобы тест не прошел случайно

