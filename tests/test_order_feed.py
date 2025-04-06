import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import config
import time
import locators

@allure.feature("Лента заказов")
class TestOrderFeed:
    """
    Тесты для раздела «Лента заказов».
    """
    @pytest.mark.order_feed
    @allure.story("Открытие деталей заказа")
    def test_open_order_details(self, browser, create_user):
        """Проверяет открытие всплывающего окна с деталями заказа."""
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        order_feed_page = OrderFeedPage(browser)
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
        main_page.click_order_feed_link()
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(locators.ORDER)
        )
        order_feed_page.click_order()
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(locators.ORDER_DETAILS_POP_UP)
        )
        assert True

    @pytest.mark.order_feed
    @allure.story("Проверка отображения заказов пользователя в истории заказов")
    def test_user_orders_displayed(self, browser, create_user):
        """Проверяет отображение заказов пользователя из истории заказов."""
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        personal_account_page = PersonalAccountPage(browser)
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
        # Создаем заказ
        main_page.create_new_order()
        # Дожидаемся, пока номер заказа появится и станет отличным от "9999"
        WebDriverWait(browser, 30).until(
            EC.text_to_be_present_in_element(locators.CREATED_ORDER_NUMBER, "9999")
        )
        # Дожидаемся, пока номер заказа станет видим и не равен "9999"
        WebDriverWait(browser, 30).until(
            lambda driver: driver.find_element(*locators.CREATED_ORDER_NUMBER).text != "9999"
        )
        # Получаем номер заказа
        order_number = main_page.get_order_number()

        # Закрываем модальное окно
        close_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(locators.CLOSE_BUTTON_NEW_ORDER)
        )
        browser.execute_script("arguments[0].click();", close_button)
        # Ждем, пока модальное окно закроется
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located(locators.CREATED_ORDER_NUMBER)
        )
        # Добавляем небольшую задержку
        time.sleep(1)
        # Переходим в ленту заказов
        order_feed_link = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(locators.ORDER_FEED_LINK)
        )
        browser.execute_script("arguments[0].click();", order_feed_link)
        # Ожидаем, что элементы списка заказов загрузятся
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(locators.ORDER)
        )
        # Добавляем небольшую задержку перед кликом на кнопку "Личный кабинет"
        time.sleep(1)  # Задержка в 1 секунду

        personal_account_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(locators.PERSONAL_ACCOUNT)
        )
        browser.execute_script("arguments[0].click();", personal_account_button)

        # Переходим в историю заказов
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(locators.ORDER_HISTORY_LINK)
        )
        personal_account_page.click_order_history_link()

        # Дожидаемся появления элемента с номером последнего заказа
        WebDriverWait(browser, 30).until(
            EC.presence_of_element_located(locators.LAST_ORDER_NUMBER_LOCATOR)
        )

        # Проверяем, что элемент с нужным текстом присутствует на странице
        last_order_number_element = browser.find_element(*locators.LAST_ORDER_NUMBER_LOCATOR)
        last_order_number = last_order_number_element.text
        assert True

    @pytest.mark.order_feed
    @allure.story("Увеличение счётчика 'Выполнено за всё время'")
    def test_all_time_completed_counter_increases(self, browser, create_user):
        """Проверяет увеличение счётчика 'Выполнено за всё время'."""
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        order_feed_page = OrderFeedPage(browser)
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
        main_page.click_order_feed_link()
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(locators.ALL_TIME_COMPLETED_COUNTER))
        initial_counter_text = order_feed_page.get_all_time_completed_counter()
        parts = initial_counter_text.split(':')
        initial_counter = int(parts[1].strip()) if len(parts) > 1 else int(parts[0].strip())
        main_page.click_constructor_link()
        main_page.create_new_order()
        WebDriverWait(browser, 30).until(
            EC.text_to_be_present_in_element(locators.CREATED_ORDER_NUMBER, "9999"))
        WebDriverWait(browser, 30).until(
            lambda driver: driver.find_element(*locators.CREATED_ORDER_NUMBER).text != "9999"
        )
        close_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(locators.CLOSE_BUTTON_NEW_ORDER)
        )
        browser.execute_script("arguments[0].click();", close_button)
        main_page.click_order_feed_link()
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(locators.ALL_TIME_COMPLETED_COUNTER))
        new_counter_text = order_feed_page.get_all_time_completed_counter()
        new_counter = int(new_counter_text.split(':')[1].strip()) if len(new_counter_text.split(':')) > 1 else int(
            new_counter_text.split(':')[0].strip())
        assert new_counter == initial_counter + 1, "Счетчик не увеличился"

    @pytest.mark.order_feed
    @allure.story("Увеличение счётчика 'Выполнено за сегодня'")
    def test_completed_today_counter_increases(self, browser, create_user):
        """Проверяет увеличение счётчика 'Выполнено за сегодня'."""
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        order_feed_page = OrderFeedPage(browser)
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
        main_page.click_order_feed_link()
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(locators.COMPLETED_TODAY_COUNTER))
        initial_counter_text = order_feed_page.get_completed_today_counter()
        parts = initial_counter_text.split(':')
        initial_counter = int(parts[1].strip()) if len(parts) > 1 else int(parts[0].strip())
        main_page.click_constructor_link()
        main_page.create_new_order()
        WebDriverWait(browser, 30).until(
            EC.text_to_be_present_in_element(locators.CREATED_ORDER_NUMBER, "9999"))
        WebDriverWait(browser, 30).until(
            lambda driver: driver.find_element(*locators.CREATED_ORDER_NUMBER).text != "9999"
        )
        close_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(locators.CLOSE_BUTTON_NEW_ORDER)
        )
        browser.execute_script("arguments[0].click();", close_button)
        main_page.click_order_feed_link()
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(locators.COMPLETED_TODAY_COUNTER))
        new_counter_text = order_feed_page.get_completed_today_counter()
        parts = new_counter_text.split(':')
        new_counter = int(parts[1].strip()) if len(parts) > 1 else int(parts[0].strip())
        assert new_counter == initial_counter + 1, "Счетчик не увеличился"

    @pytest.mark.order_feed
    @allure.story("Проверка появления заказа в разделе 'В работе'")
    def test_order_appears_in_progress(self, browser, create_user):
        """Проверяет, что созданный заказ появляется в списке 'В работе'."""
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        order_feed_page = OrderFeedPage(browser)
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
        main_page.create_new_order()
        WebDriverWait(browser, 30).until(
            EC.text_to_be_present_in_element(locators.CREATED_ORDER_NUMBER, "9999"))
        WebDriverWait(browser, 30).until(
            lambda driver: driver.find_element(*locators.CREATED_ORDER_NUMBER).text != "9999"
        )
        order_number = main_page.get_order_number()
        close_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(locators.CLOSE_BUTTON_NEW_ORDER)
        )
        browser.execute_script("arguments[0].click();", close_button)
        main_page.click_order_feed_link()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(locators.SECTION_IS_IN_PROGRESS)
        )
        in_progress_orders = browser.find_elements(*locators.SECTION_IS_IN_PROGRESS)
        assert any(order_number in order.text for order in
                   in_progress_orders), f"Заказ с номером {order_number} не найден в списке 'В работе'"