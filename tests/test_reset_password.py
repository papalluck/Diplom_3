import allure
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
import config
import logging
import pytest

logger = logging.getLogger(__name__)

@allure.feature("Восстановление пароля")
class TestResetPassword:

    @pytest.mark.reset_password
    @allure.title("Переход на страницу восстановления пароля")
    def test_navigate_to_reset_password_page(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.click_recover_password_button()
        assert login_page.is_url_correct(config.FORGOT_PASSWORD_URL), "Не удалось перейти на страницу восстановления пароля"

    @pytest.mark.reset_password
    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_restore(self, browser, create_user):
        reset_password_page = ResetPasswordPage(browser)
        reset_password_page.open()
        reset_password_page.enter_email(create_user['email'])
        reset_password_page.click_restore_button()
        assert reset_password_page.is_url_correct(config.RESET_PASSWORD_URL), "Не удалось ввести почту и нажать восстановить"

    @pytest.mark.reset_password
    @allure.title("Проверка активности поля пароля после клика по кнопке показать/скрыть пароль")
    def test_show_hide_password_button_makes_field_active(self, browser, create_user):
        login_page = LoginPage(browser)
        reset_password_page = ResetPasswordPage(browser)

        login_page.open()
        login_page.click_recover_password_button()
        assert login_page.is_url_correct(config.FORGOT_PASSWORD_URL), "Не удалось перейти на страницу восстановления пароля"

        reset_password_page.enter_email(create_user['email'])
        reset_password_page.click_restore_button()
        assert reset_password_page.is_url_correct(config.RESET_PASSWORD_URL), "Не удалось ввести почту и нажать восстановить"

        reset_password_page.enter_password("new_password")
        reset_password_page.click_show_hide_password_button()

        assert reset_password_page.is_password_field_active(), "Поле пароля не стало активным после клика на кнопку"