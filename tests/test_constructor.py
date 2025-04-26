from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from locators import Locators

class TestConstruction:

    def test_switch_to_sauce(self, driver):
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.ENTER_TO_SOUCES)).click()
        souce_list = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.SOUCES))
        assert souce_list.is_displayed()

    def test_switch_to_bun(self, driver):
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.ENTER_TO_SOUCES)).click()
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.ENTER_TO_BUNS)).click()
        buns_list = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.BUNS))
        assert buns_list.is_displayed()

    def test_switch_to_filling(self, driver):
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.ENTER_TO_FILLING)).click()
        filling_list = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.FILLINGS))
        assert filling_list.is_displayed()

