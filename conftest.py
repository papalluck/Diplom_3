import string
import logging
import pytest
import requests
import config
from helpers import random_email, random_password, generate_random_string
from utils import get_driver


logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def create_user(random_email, random_password):
    email = random_email
    password = random_password
    name = "Test User"
    user_data = {"email": email, "password": password, "name": name}
    create_user_url = f"{config.BASE_URL}/api/auth/register"

    try:
        response = requests.post(create_user_url, json=user_data)
        response.raise_for_status()
        response_data = response.json()
        if response_data and 'accessToken' in response_data:
            auth_token = response_data['accessToken']
            logger.info(f"Пользователь {email} успешно создан")
            user_data['auth_token'] = auth_token
            return user_data
        else:
            logger.warning("Ошибка: не получили access токен")
            return None

    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при создании пользователя: {e}")
        return None

    finally:
        if user_data and 'auth_token' in user_data:
            delete_user_url = f"{config.BASE_URL}/api/auth/user"
            headers = {'Authorization': f"Bearer {user_data['auth_token']}"}
            try:
                delete_response = requests.delete(delete_user_url, headers=headers)
                delete_response.raise_for_status()
                logger.info(f"Пользователь {user_data['email']} успешно удален")
            except requests.exceptions.RequestException as e:
                logger.error(f"Ошибка при удалении пользователя: {e}")


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Браузер для запуска тестов (chrome или firefox)"
    )


@pytest.fixture(scope="function")
def browser(request, create_user):
    browser_name = request.config.getoption("--browser")
    driver = get_driver(browser_name)
    driver.get(config.BASE_URL)
    yield driver
    driver.quit()