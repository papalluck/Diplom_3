from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import logging
import random


logger = logging.getLogger(__name__)


def is_order_in_progress(browser: WebDriver, order_number: str, section_locator: tuple, timeout: int = 30) -> bool:
    try:
        WebDriverWait(browser, timeout).until(
            lambda driver: any(order_number in order.text for order in driver.find_elements(*section_locator))
        )
        logger.info(f"Заказ с номером {order_number} найден в списке 'В работе'")
        return True
    except TimeoutException:
        logger.warning(f"Заказ с номером {order_number} не найден в списке 'В работе' после {timeout} секунд ожидания")
        return False

def generate_random_string(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))