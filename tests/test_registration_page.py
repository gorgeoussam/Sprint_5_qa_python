from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators, RegistrationPageLocators, ConstructorPageLocators
import helpers
import data

class TestRegistrationPage:

    def test_registration_with_valid_data_success(self, driver):
        driver.get(data.URLS["register"])
        name = helpers.generate_name()
        email = helpers.generate_email()
        password = helpers.generate_password()

        driver.find_element(*RegistrationPageLocators.INPUT_NAME_REGISTRATION).send_keys(name)
        driver.find_element(*RegistrationPageLocators.INPUT_EMAIL_REGISTRATION).send_keys(email)
        driver.find_element(*RegistrationPageLocators.INPUT_PASSWORD_REGISTRATION).send_keys(password)
        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON_REGISTRATION_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT)))

        driver.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys(email)
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys(password)
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER)))

        text_button = driver.find_element(*ConstructorPageLocators.SUBMIT_BUTTON_PLACE_AN_ORDER).text
        assert 'Оформить заказ' == text_button

    def test_registration_with_invalid_password_faill(self, driver):
        driver.get(data.URLS["register"])

        driver.find_element(*RegistrationPageLocators.INPUT_NAME_REGISTRATION).send_keys(helpers.generate_name())
        driver.find_element(*RegistrationPageLocators.INPUT_EMAIL_REGISTRATION).send_keys(helpers.generate_email())
        driver.find_element(*RegistrationPageLocators.INPUT_PASSWORD_REGISTRATION).send_keys('12345')
        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON_REGISTRATION_ACCOUNT).click()

        text_error = driver.find_element(*RegistrationPageLocators.TEXT_ERROR_PASSWORD_INPUT).text
        assert "Некорректный пароль" == text_error