import pytest
import allure
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
import config
import locators
import logging


logger = logging.getLogger(__name__)


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @pytest.mark.personal_account
    @allure.title("Переход в личный кабинет")
    def test_navigate_to_personal_account(self, browser, create_user):
        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        login_page.click_personal_account_button()
        assert personal_account_page.is_url_correct(config.ACCOUNT_URL), "Не удалось перейти в личный кабинет"

    @pytest.mark.personal_account
    @allure.title("Переход в историю заказов")
    def test_navigate_to_order_history(self, browser, create_user):
        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        login_page.click_personal_account_button()
        assert personal_account_page.is_url_correct(config.ACCOUNT_URL), "Не удалось перейти в личный кабинет"

        personal_account_page.click_order_history_link()
        assert personal_account_page.is_element_visible(locators.ORDER_HISTORY_LINK), "Не удалось перейти в историю заказов"

    @pytest.mark.personal_account
    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, browser, create_user):
        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        login_page.click_personal_account_button()
        assert personal_account_page.is_url_correct(config.ACCOUNT_URL), "Не удалось перейти в личный кабинет"

        personal_account_page.click_logout_button()
        assert login_page.is_url_correct(config.LOGIN_URL), "Не удалось выйти из аккаунта"