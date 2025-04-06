from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators, RegistrationPageLocators, ConstructorPageLocators, ForgotPasswordLocators
import data

class TestLoginPage:

    def test_login_from_main_page_via_login_button(self,
                                                   driver):  # Проверяет вход по кнопке «Войти в аккаунт» на главной
        driver.get(data.BASE_URL)
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT_MAIN_PAGE).click() # клик на кнопку «Войти в аккаунт»

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys(data.TEST_USER["email"])
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys(data.TEST_USER["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER))) # ждем кнопку оформления заказа
        text_button = driver.find_element(*ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER).text
        assert 'Оформить заказ' == text_button

    def test_login_via_personal_account_button(self, driver):  # Проверяет вход через кнопку «Личный кабинет»
        driver.get(data.BASE_URL)
        driver.find_element(*LoginPageLocators.BUTTON_PERSONAL_ACCOUNT).click() # клик на кнопку «Личный кабинет»

        #авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys(data.TEST_USER["email"])
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys(data.TEST_USER["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER))) # ждем кнопку оформления заказа
        text_button = driver.find_element(*ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER).text
        assert 'Оформить заказ' == text_button

    def test_login_via_registration_form_button(self, driver):  # Проверяет вход через кнопку войти в форме регистрации
        driver.get(data.URLS['register'])
        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON_REGISTRATION_FORM).click() # кнопка "войти" в форме регистрации

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys(data.TEST_USER["email"])
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys(data.TEST_USER["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER))) # ждем кнопку оформления заказа на главной
        text_button = driver.find_element(*ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER).text
        assert 'Оформить заказ' == text_button

    def test_login_via_password_recovery_form_button(self,
                                                     driver):  # Проверяет вход через кнопку в форме восстановления пароля
        driver.get(data.URLS['forgot-password'])
        driver.find_element(*ForgotPasswordLocators.SUBMIT_BUTTON_FORGOT_FORM).click() # кнопка "войти" в форме восстановления пароля

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys(data.TEST_USER["email"])
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys(data.TEST_USER["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()


        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER))) # ждем кнопку оформления заказа на главной
        text_button = driver.find_element(*ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER).text
        assert 'Оформить заказ' == text_button

    def test_logout_button_in_personal_account(self, driver): # проверяет выход по кнопке «Выйти» в личном кабинете
        driver.get(data.URLS["login"])

        # авторизация
        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys(data.TEST_USER["email"])
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys(data.TEST_USER["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER)))  # ждем кнопку оформления заказа на главной

        driver.find_element(*LoginPageLocators.BUTTON_PERSONAL_ACCOUNT).click() # клик по кнопке «Личный кабинет»

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (LoginPageLocators.BUTTON_LOGOUT_ACCOUNT))) # ждем появления кнопки выхода из профиля

        driver.find_element(*LoginPageLocators.BUTTON_LOGOUT_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (LoginPageLocators.TEXT_AUTH_LOGIN))) # ждем появления формы входа

        text_button = driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).text
        assert "Войти" == text_button