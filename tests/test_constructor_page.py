from locators import  ConstructorPageLocators
import data

class TestConstructorPage:
    def test_navigate_to_buns_section(self, driver): # переход к разделу булки
        driver.get(data.BASE_URL)
        driver.find_element(*ConstructorPageLocators.TAB_FILLINGS).click() # Сначала переходим в начинки, таб булки выделен по умолчанию
        driver.find_element(*ConstructorPageLocators.TAB_BUNS).click() # возвращаемся в булки

        buns_tab = driver.find_element(*ConstructorPageLocators.TAB_BUNS_SELECT)

        assert "tab_type_current" in buns_tab.get_attribute('class')


    def test_navigate_to_sauces_section(self, driver): # переход к разделу соус
        driver.get(data.BASE_URL)
        driver.find_element(*ConstructorPageLocators.TAB_SAUCES).click()

        sauces_tab = driver.find_element(*ConstructorPageLocators.TAB_SAUCES_SELECT)

        assert "tab_type_current" in sauces_tab.get_attribute('class')

    def test_navigate_to_fillings_section(self, driver): # переход к разделу начинки
        driver.get(data.BASE_URL)
        driver.find_element(*ConstructorPageLocators.TAB_FILLINGS).click()

        fillings_tab =  driver.find_element(*ConstructorPageLocators.TAB_FILLINGS_SELECT)

        assert "tab_type_current" in fillings_tab.get_attribute('class')