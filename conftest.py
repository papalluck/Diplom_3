import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import config
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators

def generate_random_email():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return f"{random_string}@example.com"

def generate_random_password():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(12))

@pytest.fixture(scope="session")
def create_user():
    email = generate_random_email()
    password = generate_random_password()
    name = "Test User"
    user_data = {"email": email, "password": password, "name": name}
    create_user_url = f"{config.BASE_URL}/api/auth/register"
    auth_token = None  # Store the auth token

    try:
        response = requests.post(create_user_url, json=user_data)
        response.raise_for_status()
        response_data = response.json()
        if response_data and 'accessToken' in response_data:
                auth_token = response_data['accessToken'].split(' ')[1]
                print(f"Пользователь {email} успешно создан")
                user_data['auth_token'] = auth_token
                yield user_data
        else:
            print("Ошибка: не получили access токен")
            yield None

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при создании пользователя: {e}")
        yield None
    finally:
        if user_data and 'auth_token' in user_data:
            delete_user_url = f"{config.BASE_URL}/api/auth/user"
            headers = {'Authorization': f"Bearer {user_data['auth_token']}"}
            try:
                delete_response = requests.delete(delete_user_url, headers=headers)
                delete_response.raise_for_status()
                print(f"Пользователь {user_data['email']} успешно удален")
            except requests.exceptions.RequestException as e:
                print(f"Ошибка при удалении пользователя: {e}")


def get_driver(browser_name):
    if browser_name == "chrome":
        chrome_options = Options()
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")

    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Браузер для запуска тестов (chrome или firefox)"
    )


@pytest.fixture(scope="function")
def browser(request, create_user):
    browser_name = request.config.getoption("--browser")
    driver = get_driver(browser_name)
    if create_user:
        driver.get("https://stellarburgers.nomoreparties.site/")
        from pages.login_page import LoginPage
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
    else:
         driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()