from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//a[@href='/account']")  # кнопка входа в личный кабинет
    SUBMIT_BUTTON_LOGIN_TO_ACCOUNT_MAIN_PAGE = (
    By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # кнопка входа в аккаунт на главной
    SUBMIT_BUTTON_LOGIN_TO_ACCOUNT = (
    By.XPATH, ".//button[text() = 'Войти']")  # кнопка входа в аккаунт на странице login
    INPUT_EMAIL_LOGIN = (By.XPATH, ".//input[@type='text']")  # поле ввода email на странице входа
    INPUT_PASSWORD_LOGIN = (By.XPATH, ".//input[@type='password']")  # поле ввода email на странице регистрации
    BUTTON_LOGOUT_ACCOUNT  = (By.XPATH, ".//button[contains(@class, 'Account_button')]")  # кнопка выхода из аккаунта в личном кабинете
    TEXT_AUTH_LOGIN = (By.XPATH, ".//h2[text() = 'Вход']")


class RegistrationPageLocators:
    SUBMIT_BUTTON_REGISTRATION_ACCOUNT = (
    By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # кнопка зарегистироваться на странцие регистрации
    SUBMIT_BUTTON_ACCOUNT_RECOVERY = (
    By.XPATH, ".//button[text() = 'Восстановить']")  # кнопка восстановления пароля на странице восстановления
    INPUT_NAME_REGISTRATION = (
    By.XPATH, ".//label[text()='Имя']/following-sibling::input")  # поле ввода имени на странице регистрации
    INPUT_EMAIL_REGISTRATION = (
    By.XPATH, ".//label[text()='Email']/following-sibling::input")  # поле ввода email на странице регистрации
    INPUT_PASSWORD_REGISTRATION = (
    By.XPATH, ".//input[@type='password']")  # поле ввода пароля на странице регистрации
    TEXT_ERROR_PASSWORD_INPUT = (By.XPATH,
                                 ".//p[contains(@class, 'input__error')]")  # сообщение о неккоректном пароле на странице регистрации
    SUBMIT_BUTTON_REGISTRATION_FORM = (
    By.XPATH, ".//p[text() = 'Уже зарегистрированы?']/a")  # Кнопка войти в форме регистрации


class ForgotPasswordLocators:
    SUBMIT_BUTTON_FORGOT_FORM = (
    By.XPATH, ".//p[text() = 'Вспомнили пароль?']/a")  # Кнопка войти в форме восстановления пароля


class ProfilePageLocators:
    ACCOUNT_TEXT_IN_PROFILE = (By.XPATH, ".//p[contains(@class, 'Account_text')]") # текст на странице профиля


class ConstructorPageLocators:
    SUBMIT_BUTTON_PLACE_AN_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    CONSTRUCTOR_BUTTON = (By.XPATH, './/a[@href="/"]/p')  # кнопка перехода на страницу с конструктором
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[contains(@class, 'text')]")
    CONSTRUCTOR_LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]")

    TAB_BUNS = (By.XPATH, ".//span[text()='Булки']")  # таб булки на главной
    TAB_SAUCES = (By.XPATH, ".//span[text()='Соусы']")  # таб соусы на главной
    TAB_FILLINGS = (By.XPATH, ".//span[text()='Начинки']")  # таб начинки на главной

    TAB_BUNS_SELECT = (By.XPATH, ".//span[text()='Булки']/..")  # таб булки на главной выбранный
    TAB_SAUCES_SELECT = (By.XPATH, ".//span[text()='Соусы']/..")  # таб соусы на главной выбранный
    TAB_FILLINGS_SELECT = (By.XPATH, ".//span[text()='Начинки']/..")  # таб начинки на главной выбранный