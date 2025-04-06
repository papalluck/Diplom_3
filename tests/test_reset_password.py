import pytest
import allure
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import locators

@allure.feature("Восстановление пароля")
class TestResetPassword:
    """
    Класс для тестов восстановления пароля.
    """
    @allure.story("Переход на страницу восстановления пароля")
    def test_navigate_to_reset_password_page(self, browser):
        """
        Проверяет переход на страницу восстановления пароля по кнопке «Восстановить пароль».
        """
        login_page = LoginPage(browser)
        login_page.open()
        login_page.click_recover_password_button()
        WebDriverWait(browser, 10).until(
            EC.url_to_be(config.FORGOT_PASSWORD_URL)
        )
        assert browser.current_url == config.FORGOT_PASSWORD_URL, "Не произошел переход на страницу восстановления пароля"

    @allure.story("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_restore(self, browser, create_user):
        """
        Проверяет ввод почты и клик по кнопке «Восстановить».
        """
        reset_password_page = ResetPasswordPage(browser)
        reset_password_page.open()
        reset_password_page.enter_email(create_user['email'])  # Используем email созданного пользователя
        reset_password_page.click_restore_button()
        WebDriverWait(browser, 10).until(
            EC.url_to_be(config.RESET_PASSWORD_URL)
        )
        assert browser.current_url == config.RESET_PASSWORD_URL, "Не произошел переход на страницу сброса пароля"

    @allure.story("Проверка активности поля пароля после клика по кнопке показать/скрыть пароль")
    def test_show_hide_password_button_makes_field_active(self, browser, create_user):
        """
        Проверяет, что клик по кнопке показать/скрыть пароль делает поле активным.
        """
        login_page = LoginPage(browser)
        reset_password_page = ResetPasswordPage(browser)

        # 1. Нажимаем "Войти в аккаунт"
        login_page.open()

        # 2. Нажимаем "Восстановить пароль"
        login_page.click_recover_password_button()
        WebDriverWait(browser, 10).until(
            EC.url_to_be(config.FORGOT_PASSWORD_URL)
        )

        # 3. Вводим валидный email
        reset_password_page.enter_email(create_user['email'])

        # 4. Нажимаем кнопку "Восстановить"
        reset_password_page.click_restore_button()
        WebDriverWait(browser, 10).until(
            EC.url_to_be(config.RESET_PASSWORD_URL)
        )

        # 5. Вводим валидный пароль
        reset_password_page.enter_password("new_password") # хардкод пароля

        # 6. Нажимаем на кнопку "показать/скрыть пароль"
        reset_password_page.click_show_hide_password_button()

        # 7. Проверяем, что поле пароля активно
        assert reset_password_page.is_password_field_active(), "Поле пароля не стало активным после клика на кнопку"