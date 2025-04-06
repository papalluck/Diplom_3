from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
import config


class ResetPasswordPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = config.RESET_PASSWORD_URL

    def open(self):
        self.browser.get(self.url)

    def enter_email(self, email):
        # Явное ожидание
        email_field = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.EMAIL_INPUT)
        )

        # Клик по полю
        email_field.click()

        # Ввод email
        email_field.send_keys(email)

    def click_restore_button(self):
        restore_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.RESTORE_BUTTON)
        )
        restore_button.click()

    def enter_password(self, password):
        # Явное ожидание
        password_field = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.PASSWORD_INPUT)
        )

        # Клик по полю
        password_field.click()

        # Ввод password
        password_field.send_keys(password)

    def click_save_button(self):
        save_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.SAVE_BUTTON)
        )
        save_button.click()

    def click_show_hide_password_button(self):
        show_hide_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.SHOW_HIDE_PASSWORD_BUTTON)
        )
        show_hide_button.click()

    def is_password_field_active(self):
        try:
            active_password_field = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locators.ACTIVE_PASSWORD_FIELD)
            )
            return True
        except:
            return False

    def is_save_button_displayed(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locators.SAVE_BUTTON)
            )
            return True
        except:
            return False