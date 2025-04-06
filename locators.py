from selenium.webdriver.common.by import By

# Login Page Locators
LOGIN_BUTTON = (By.XPATH, "//font[contains(text(),'Войти в аккаунт')]")
PERSONAL_ACCOUNT = (By.XPATH, "//div/header/nav/a")
BUTTON_RECOVER_PASSWORD = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
SIGN_IN_BUTTON = (By.XPATH, "//button[@class ='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
EMAIL_INPUT = (By.XPATH, "//div/main/div/form/fieldset/div/div/input")
PASSWORD_FIELD = (By.XPATH, "//div/main/div/form/fieldset[2]/div/div/input")  # Для страницы ЛОГИНА

# Reset Password Page Locators
RESTORE_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
SAVE_BUTTON = (By.XPATH, "//button[@class ='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")  # Кнопка "Сохранить"
SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div/main/div/form/fieldset[1]/div/div/div")
ACTIVE_PASSWORD_FIELD = (By.XPATH, "//div[contains(@class,'input_status_active')] // input[@ name='Введите новый пароль']")  # Используйте этот локатор для проверки активности
PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")  # Для страницы СБРОСА ПАРОЛЯ

# Personal Account Page Locators
ORDER_HISTORY_LINK = (By.XPATH, "//div/main/div/nav/ul/li[2]/a") # радел история заказов
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]") # кнопка выход из аккаунта
EMAIL_FIELD = (By.XPATH, "//div/main/div/form/fieldset[1]/div/div/input") # поле email

# Основной функционал
CONSTRUCTOR_LINK = (By.XPATH, "//div/header/nav/ul/li[1]/a") # раздел конструктор
ACTIVE_CONSTRUCTOR_LINK = (By.XPATH, "//div/header/nav/ul/li[1]/a") # активный раздел конструктор
ORDER_FEED_LINK = (By.XPATH, "//div/header/nav/ul/li[2]/a/p") # раздел лента заказов
FLUORESCENT_BUN = (By.XPATH, "//div/main/section[1]/div[2]/ul[1]/a[1]/p") # ингредиент флюоресцентная булка
CLOSE_BUTTON = (By.XPATH, "//div/section[1]/div[1]/button") # кнопка закрыть(крестик)
INGREDIENT_COUNTER = (By.XPATH, "//div/main/section[1]/div[2]/ul[2]/a[1]/div[1]/p") # каунтер ингредиента
SAUCE_SPICY_X = (By.XPATH, "//div/main/section[1]/div[2]/ul[2]/a[1]/img") # соус Spicy-X
CHECKOUT_BUTTON = (By.XPATH, "//div/main/section[2]/div/button") # кнопка оформить заказ
INGREDIENT_DETAILS = (By.XPATH, "//div/section[1]/div[1]/div/h2") # детали ингредиента
YOUR_ORDER_HAS_BEEN_PREPARED = (By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']") # надпись "ваш заказ начали готовить" в окне созданного заказа
BURGER_CONSTRUCTOR_BASKET = (By.XPATH, "//div/main/section[2]/ul") # корзина для ингредиентов

# Лента заказов
ORDER = (By.XPATH, "//div/main/div/div/ul/li[1]") # 1 заказ из ленты
ORDERS_HISTORY = (By.XPATH, "//div/main/div/div/div/ul/li[44]/a/div[1]") # история заказов из личного кабинета
ORDER_FEED_LIST = (By.XPATH, "//div/main/div/div/ul") # список заказов из ленты
ALL_TIME_COMPLETED_COUNTER = (By.XPATH, "//div/main/div/div/div/div[2]/p[2]") # счётчик выполнено за всё время
COMPLETED_TODAY_COUNTER = (By.XPATH, "//div/main/div/div/div/div[3]/p[2]") # счётчик выполнено за сегодня
SECTION_IS_IN_PROGRESS = (By.XPATH, "//div/main/div/div/div/div[1]/ul[1]/li[1]") # раздел в работе ленты заказов
ORDER_DETAILS_POP_UP = (By.XPATH, "//div/section[2]/div[1]") # всплывающее окно с деталями заказа
CLOSE_BUTTON_NEW_ORDER = (By.XPATH, "//div/section/div[1]/button") # кнопка закрыть всплывающее окно созданного заказа
CREATED_ORDER_NUMBER = (By.XPATH, "//div/section/div[1]/div/h2") # номер созданного заказа
LAST_ORDER_NUMBER_LOCATOR = (By.XPATH, "//div/main/div/div/div/ul/li[1]/a/div[1]")