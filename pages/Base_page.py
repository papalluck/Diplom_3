from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.browser.get(url)

    @allure.step("Кликаем на элемент: {locator}")
    def click(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="screenshot_after_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Не удалось кликнуть на элемент {locator} за {timeout} секунд")

    @allure.step("Вводим текст '{text}' в поле: {locator}")
    def send_keys(self, locator, text, timeout=10):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="screenshot_after_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Не удалось ввести текст в поле {locator} за {timeout} секунд")

    @allure.step("Проверяем, что URL соответствует: {url}")
    def is_url_correct(self, url, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.url_to_be(url))
            return True
        except TimeoutException:
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="screenshot_after_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Текущий URL не соответствует ожидаемому {url} за {timeout} секунд")

    @allure.step("Проверяем, что элемент виден: {locator}")
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="screenshot_after_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Элемент {locator} не виден на странице за {timeout} секунд")

    @allure.step("Проверяем, что элемент не виден: {locator}")
    def is_element_invisible(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="screenshot_after_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Элемент {locator} все еще виден на странице за {timeout} секунд")

    @allure.step(f"Проверяем, что element_to_be_clickable : {{locator}}")
    def element_to_be_clickable(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="screenshot_after_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"element_to_be_clickable {locator} все еще виден на странице за {timeout} секунд")