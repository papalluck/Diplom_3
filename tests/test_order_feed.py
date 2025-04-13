import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
import logging
import re

logger = logging.getLogger(__name__)


@allure.feature("Лента заказов")
class TestOrderFeed:
    @pytest.mark.order_feed
    @allure.title("Открытие деталей заказа")
    def test_open_order_details(self, browser, create_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        order_feed_page = OrderFeedPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        main_page.click_order_feed_link()
        order_feed_page.click_order()
        assert order_feed_page.is_order_details_displayed(), "Не удалось открыть детали заказа"

    @pytest.mark.order_feed
    @allure.title("Проверка отображения заказов пользователя в истории заказов")
    def test_user_orders_displayed(self, browser, create_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        personal_account_page = PersonalAccountPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        order_number = main_page.create_new_order()

        login_page.click_personal_account_button()
        personal_account_page.click_order_history_link()

        last_order_number = personal_account_page.get_last_order_number()

        assert order_number in last_order_number, f"Ожидаемый номер заказа {order_number} не найден в истории заказов. Фактический список: {last_order_number}"

    @pytest.mark.order_feed
    @allure.title("Увеличение счётчика 'Выполнено за всё время'")
    def test_all_time_completed_counter_increases(self, browser, create_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        order_feed_page = OrderFeedPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        main_page.click_order_feed_link()
        assert order_feed_page.is_all_time_completed_counter_displayed(), "Не отображается счетчик 'Выполнено за всё время'"
        initial_counter_text = order_feed_page.get_all_time_completed_counter()
        initial_counter = int(re.search(r'\d+', initial_counter_text).group())

        main_page.click_constructor_link()

        order_number = main_page.create_new_order()

        main_page.click_order_feed_link()
        assert order_feed_page.is_all_time_completed_counter_displayed(), "Не отображается счетчик 'Выполнено за всё время'"
        new_counter_text = order_feed_page.get_all_time_completed_counter()
        new_counter = int(re.search(r'\d+', new_counter_text).group())

        assert new_counter == initial_counter + 1, "Счетчик не увеличился"

    @pytest.mark.order_feed
    @allure.title("Увеличение счётчика 'Выполнено за сегодня'")
    def test_completed_today_counter_increases(self, browser, create_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        order_feed_page = OrderFeedPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        main_page.click_order_feed_link()
        assert order_feed_page.is_completed_today_counter_displayed(), "Не отображается счетчик 'Выполнено за сегодня'"
        initial_counter_text = order_feed_page.get_completed_today_counter()
        initial_counter = int(re.search(r'\d+', initial_counter_text).group())

        main_page.click_constructor_link()

        order_number = main_page.create_new_order()

        main_page.click_order_feed_link()
        assert order_feed_page.is_completed_today_counter_displayed(), "Не отображается счетчик 'Выполнено за сегодня'"
        new_counter_text = order_feed_page.get_completed_today_counter()
        new_counter = int(re.search(r'\d+', new_counter_text).group())

        assert new_counter == initial_counter + 1, "Счетчик не увеличился"

    @pytest.mark.order_feed
    @allure.title("Проверка появления заказа в разделе 'В работе'")
    def test_order_appears_in_progress(self, browser, create_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        order_feed_page = OrderFeedPage(browser)

        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()

        order_number = main_page.create_new_order()

        logger.info(f"Номер заказа: {order_number}")

        main_page.click_order_feed_link()

        order_feed_page.wait_for_order_in_progress(order_number)

        assert order_feed_page.is_order_present_in_progress(order_number), f"Заказ с номером {order_number} не найден в списке 'В работе'"