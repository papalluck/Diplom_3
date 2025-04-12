from selenium.webdriver.common.by import By

# Login Page Locators
LOGIN_BUTTON = (By.XPATH, "//font[contains(text(),'Войти в аккаунт')]")
PERSONAL_ACCOUNT = (By.XPATH, "//a[@href='/account']")
BUTTON_RECOVER_PASSWORD = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
SIGN_IN_BUTTON = (By.XPATH, "//button[@class ='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")

# Reset Password Page Locators
RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']//*[name()='svg']")
ACTIVE_PASSWORD_FIELD = (By.XPATH, "//div[contains(@class,'input_status_active')] // input[@ name='Введите новый пароль']")
PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")

# Personal Account Page Locators
ORDER_HISTORY_LINK = (By.XPATH, "//li[@class='Account_listItem__35dAP']//a[@href='/account/order-history']")
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
EMAIL_FIELD = (By.XPATH, "//font[contains(text(),'Электронная почта')]")

# Основной функционал
CONSTRUCTOR_LINK = (By.XPATH, "//ul[@class ='AppHeader_header__list__3oKJj']//a[@href='/']")
ACTIVE_CONSTRUCTOR_LINK = (By.XPATH, "//ul[@class ='AppHeader_header__list__3oKJj']//a[@href='/']")
ORDER_FEED_LINK = (By.XPATH, "//ul[@class='AppHeader_header__list__3oKJj']//a[@href='/feed']")
FLUORESCENT_BUN = (By.XPATH, "//a[@href= '/ingredient/61c0c5a71d1f82001bdaaa6d']//p[@class= 'BurgerIngredient_ingredient__text__yp3dH']")
CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
INGREDIENT_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']//p[@class='counter_counter__num__3nue1']")
SAUCE_SPICY_X = (By.XPATH, "//img[@alt='Соус Spicy-X']")
CHECKOUT_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
INGREDIENT_DETAILS = (By.XPATH, "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']")
YOUR_ORDER_HAS_BEEN_PREPARED = (By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']")
BURGER_CONSTRUCTOR_BASKET = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")

# Лента заказов
ORDER = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']//a[@class='OrderHistory_link__1iNby']")
ORDERS_HISTORY = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")
ORDER_FEED_LIST = (By.XPATH, "//ul[@class='OrderFeed_list__OLh59']")
ALL_TIME_COMPLETED_COUNTER = (By.XPATH, "//div[@class='undefined mb-15']/descendant::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
COMPLETED_TODAY_COUNTER = (By.XPATH, "//p[@class='text text_type_main-medium' and text()='Выполнено за сегодня:']/following-sibling::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
SECTION_IS_IN_PROGRESS = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li")
ORDER_DETAILS_POP_UP = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
CLOSE_BUTTON_NEW_ORDER = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
CREATED_ORDER_NUMBER = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
LAST_ORDER_NUMBER_LOCATOR = (By.XPATH, "//a[@class='OrderHistory_link__1iNby']//p[@class='text text_type_digits-default'][last()]")