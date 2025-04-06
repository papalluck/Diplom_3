from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
import config


class PersonalAccountPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = config.ACCOUNT_URL  #  Используем URL личного кабинета из config

    def open(self):
        self.browser.get(self.url)

    def click_order_history_link(self):
        order_history_link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.ORDER_HISTORY_LINK)
        )
        order_history_link.click()

    def click_logout_button(self):
        logout_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locators.LOGOUT_BUTTON)
        )
        logout_button.click()

    def is_logout_button_displayed(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locators.LOGOUT_BUTTON)
            )
            return True
        except:
            return False

