from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common.exceptions import TimeoutException
import re


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.browser.get(url)

    @allure.step("Кликаем на элемент: {locator}")
    def click(self, locator, timeout=20):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Не удалось кликнуть на элемент {locator} за {timeout} секунд")

    @allure.step("Вводим текст '{text}' в поле: {locator}")
    def send_keys(self, locator, text, timeout=20):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Не удалось ввести текст в поле {locator} за {timeout} секунд")

    @allure.step("Проверяем, что URL соответствует: {url}")
    def is_url_correct(self, url, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.url_to_be(url))
            return True
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Текущий URL не соответствует ожидаемому {url} за {timeout} секунд")

    @allure.step("Проверяем, что элемент виден: {locator}")
    def is_element_visible(self, locator, timeout=20):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Элемент {locator} не виден на странице за {timeout} секунд")

    @allure.step("Проверяем, что элемент не виден: {locator}")
    def is_element_invisible(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Элемент {locator} все еще виден на странице за {timeout} секунд")

    @allure.step("Проверяем, что элемент кликабелен: {locator}")
    def element_to_be_clickable(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Элемент {locator} не кликабелен на странице за {timeout} секунд")

    def attach_screenshot(self):
        allure.attach(
            self.browser.get_screenshot_as_png(),
            name="screenshot_after_timeout",
            attachment_type=allure.attachment_type.PNG
        )

    def find_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Элемент {locator} не найден на странице за {timeout} секунд")

    def find_elements(self, locator, timeout=10):
        try:
            elements = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Элементы {locator} не найдены на странице за {timeout} секунд")

    @allure.step("Ожидаем, пока текст элемента не изменится")
    def wait_for_text_to_change(self, locator, initial_text, timeout=30):
        try:
            WebDriverWait(self.browser, timeout).until(
                lambda driver: self.find_element(locator).text != initial_text
            )
            return True
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Не дождались изменения текста элемента {locator} за {timeout} секунд")

    @allure.step("Ожидаем, пока элемент станет видимым")
    def wait_for_element_visibility(self, locator, timeout=30):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Не дождались видимости элемента {locator} за {timeout} секунд")

    @allure.step("Ожидаем, пока текст элемента изменится с одного значения на другое")
    def wait_for_text_to_be_different(self, locator, text_to_be_different, timeout=30):
        try:
            WebDriverWait(self.browser, timeout).until(
                lambda driver: self.find_element(locator).text != text_to_be_different
            )
            return True
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(
                f"Не дождались изменения текста элемента {locator} с {text_to_be_different} за {timeout} секунд")

    @allure.step("Ожидаем пока элемент с текстом станет видимым")
    def wait_until_text_present(self, locator, text, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Не дождались появления текста '{text}' в элементе {locator} за {timeout} секунд")

    @allure.step("Ожидаем, пока текст элемента соответствует регулярному выражению")
    def wait_for_text_to_match_regex(self, locator, regex, timeout=30):
        try:
            WebDriverWait(self.browser, timeout).until(
                lambda driver: re.match(regex, self.find_element(locator).text)
            )
            return True
        except TimeoutException:
            self.attach_screenshot()
            raise TimeoutException(f"Не дождались, пока текст элемента {locator} будет соответствовать регулярному выражению '{regex}' за {timeout} секунд")