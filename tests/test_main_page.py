import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
import config
import logging

logger = logging.getLogger(__name__)


@allure.feature("Основная страница")
class TestMainPage:
    @pytest.mark.main_page
    @allure.title("Переход в конструктор")
    def test_navigate_to_constructor(self, browser, create_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        main_page.click_constructor_link()
        assert main_page.is_constructor_link_active(), "Не удалось перейти в конструктор"

    @pytest.mark.main_page
    @allure.title("Переход в ленту заказов")
    def test_navigate_to_order_feed(self, browser, create_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        main_page.click_order_feed_link()
        assert main_page.is_url_correct(config.ORDER_FEED_URL), "Не удалось перейти в ленту заказов"

    @pytest.mark.main_page
    @allure.title("Открытие всплывающего окна ингредиента")
    def test_open_ingredient_popup(self, browser, create_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        main_page.click_ingredient()
        assert main_page.is_ingredient_popup_visible(), "Не удалось открыть всплывающее окно ингредиента"

    @pytest.mark.main_page
    @allure.title("Закрытие всплывающего окна ингредиента")
    def test_close_ingredient_popup(self, browser, create_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        main_page.click_ingredient()
        main_page.click_close_button()
        assert main_page.is_ingredient_popup_invisible(), "Не удалось закрыть всплывающее окно ингредиента"

    @pytest.mark.main_page
    @allure.title("Добавление ингредиента и увеличение счетчика")
    def test_add_ingredient_counter(self, browser, create_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        main_page.drag_and_drop_sauce()
        main_page.drag_and_drop_sauce()
        main_page.drag_and_drop_sauce()

        counter_value = main_page.get_ingredient_counter()
        assert counter_value == "3", f"Ожидалось значение счетчика 3, получено: {counter_value}"

    @pytest.mark.main_page
    @allure.title("Оформление заказа залогиненным пользователем")
    def test_checkout_logged_in(self, browser, create_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        main_page.click_checkout_button()
        assert main_page.is_checkout_successful(), "Не появилось сообщение об успешном оформлении заказа"