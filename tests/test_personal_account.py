import pytest
import allure
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import locators

@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.story("Переход в личный кабинет")
    def test_navigate_to_personal_account(self, browser, create_user):

        login_page = LoginPage(browser)
        login_page.open()

        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(locators.EMAIL_INPUT)
        )
        login_page.enter_email(create_user['email'])
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(locators.PASSWORD_FIELD)
        )
        login_page.enter_password(create_user['password'])

        login_page.click_login_button()

        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(locators.PERSONAL_ACCOUNT)
        )
        login_page.click_personal_account_button()

        WebDriverWait(browser, 20).until(
            EC.url_to_be(config.ACCOUNT_URL)
        )
        assert browser.current_url == config.ACCOUNT_URL

    @allure.story("Переход в историю заказов")
    def test_navigate_to_order_history(self, browser, create_user):

        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)
        login_page.open()

        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(locators.PERSONAL_ACCOUNT)
        )
        login_page.click_personal_account_button()

        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(locators.EMAIL_INPUT)
        )
        login_page.enter_email(create_user['email'])
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(locators.PASSWORD_FIELD)
        )
        login_page.enter_password(create_user['password'])

        login_page.click_login_button()

        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(locators.PERSONAL_ACCOUNT)
        )
        login_page.click_personal_account_button()

        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(locators.ORDER_HISTORY_LINK)
        )
        personal_account_page.click_order_history_link()

        WebDriverWait(browser, 20).until(
            EC.url_to_be(config.ORDER_HISTORY_URL)
        )
        assert browser.current_url == config.ORDER_HISTORY_URL

    @allure.story("Выход из аккаунта")
    def test_logout_from_account(self, browser, create_user):

        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)
        login_page.open()

        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(locators.PERSONAL_ACCOUNT)
        )
        login_page.click_personal_account_button()

        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(locators.EMAIL_INPUT)
        )
        login_page.enter_email(create_user['email'])
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(locators.PASSWORD_FIELD)
        )
        login_page.enter_password(create_user['password'])

        login_page.click_login_button()

        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(locators.PERSONAL_ACCOUNT)
        )
        login_page.click_personal_account_button()

        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(locators.LOGOUT_BUTTON)
        )
        personal_account_page.click_logout_button()

        WebDriverWait(browser, 20).until(EC.url_to_be(config.LOGIN_URL))
        assert browser.current_url == config.LOGIN_URL