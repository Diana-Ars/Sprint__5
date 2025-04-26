from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestPersonalAcc:

    def test_enter_personal_acc(self, login):
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON)).click()
        response = WebDriverWait(login, 5).until(EC.visibility_of_element_located(Locators.PROFILE_TEXT))
        assert response.is_displayed()


    def test_switch_from_personal_acc_to_constructor_by_constructor(self, login):
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON)).click()
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.ENTER_CONSTRUCTOR)).click()
        response = WebDriverWait(login, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TEXT))
        assert response.is_displayed()


    def test_switch_from_personal_acc_to_constructor_by_logo(self, login):
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON)).click()
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.ENTER_BY_LOGO)).click()
        response = WebDriverWait(login, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TEXT))
        assert response.is_displayed()


    def test_log_out_from_acc(self, login):
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON)).click()
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.LOG_OUT)).click()
        response = WebDriverWait(login, 5).until(EC.visibility_of_element_located(Locators.ENTER_TEXT))
        assert response.is_displayed()


