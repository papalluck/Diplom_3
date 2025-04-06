import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import locators

@allure.feature("Основная страница")
class TestMainPage:
    """
    Тесты для основной страницы.
    """
    @pytest.mark.main_page
    @allure.story("Переход в конструктор")
    def test_navigate_to_constructor(self, browser, create_user):
        """Проверяет переход в конструктор."""
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        # Логинимся
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
        main_page.click_constructor_link()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(locators.ACTIVE_CONSTRUCTOR_LINK)
        )
        assert True

    @pytest.mark.main_page
    @allure.story("Переход в ленту заказов")
    def test_navigate_to_order_feed(self, browser, create_user):
        """Проверяет переход по клику на «Лента заказов»."""
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        # Логинимся
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
        # Переходим в ленту заказов
        main_page.click_order_feed_link()
        WebDriverWait(browser, 10).until(
            EC.url_to_be(config.ORDER_FEED_URL)
        )
        assert True

    @pytest.mark.main_page
    @allure.story("Открытие всплывающего окна ингредиента")
    def test_open_ingredient_popup(self, browser, create_user):
        """Проверяет открытие всплывающего окна ингредиента."""
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        # Логинимся
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
        # Кликаем на ингредиент
        main_page.click_ingredient()
        # Проверяем, что появилось всплывающее окно
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(locators.INGREDIENT_DETAILS)
        )
        assert True

    @pytest.mark.main_page
    @allure.story("Закрытие всплывающего окна ингредиента")
    def test_close_ingredient_popup(self, browser, create_user):
        """Проверяет закрытие всплывающего окна ингредиента."""
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        # Логинимся
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
        # Кликаем на ингредиент, чтобы открыть всплывающее окно
        main_page.click_ingredient()
        # Кликаем на кнопку закрытия
        main_page.click_close_button()
        # Проверяем, что всплывающее окно исчезло
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located(locators.INGREDIENT_DETAILS)
        )
        assert True

    @pytest.mark.main_page
    @allure.story("Добавление ингредиента и увеличение счетчика")
    def test_add_ingredient_counter(self, browser, create_user):
        """Проверяет увеличение счетчика ингредиента при добавлении в заказ."""
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        # Логинимся
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        # Добавляем 3 соуса перетаскиванием
        main_page.drag_and_drop_ingredient(locators.SAUCE_SPICY_X)
        main_page.drag_and_drop_ingredient(locators.SAUCE_SPICY_X)
        main_page.drag_and_drop_ingredient(locators.SAUCE_SPICY_X)

        # Проверяем, что значение счетчика равно 3
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(locators.INGREDIENT_COUNTER, "3")
        )
        assert True

    @pytest.mark.main_page
    @allure.story("Оформление заказа залогиненным пользователем")
    def test_checkout_logged_in(self, browser, create_user):
        """Проверяет возможность оформления заказа залогиненным пользователем."""
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        # Логинимся
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
        # Кликаем на кнопку "Оформить заказ"
        main_page.click_checkout_button()
        # Проверяем, что появилась надпись "Ваш заказ начали готовить"
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(locators.YOUR_ORDER_HAS_BEEN_PREPARED)
        )
        assert True