from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locators


class TestPersonalAcc:

    def test_enter_personal_acc(self, login):
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON)).click()
        response = WebDriverWait(login, 5).until(EC.text_to_be_present_in_element((By.XPATH, '//main'), 'Профиль'))
        assert response == True
        login.quit()

    def test_switch_from_personal_acc_to_constructor_by_constructor(self, login):
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON)).click()
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.ENTER_CONSTRUCTOR)).click()
        response = WebDriverWait(login, 5).until(EC.text_to_be_present_in_element((By.XPATH, '//main'), 'Соберите бургер'))
        assert response == True
        login.quit()

    def test_switch_from_personal_acc_to_constructor_by_logo(self, login):
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON)).click()
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.ENTER_BY_LOGO)).click()
        response = WebDriverWait(login, 5).until(EC.text_to_be_present_in_element((By.XPATH, '//main'), 'Соберите бургер'))
        assert response == True
        login.quit()

    def test_log_out_from_acc(self, login):
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON)).click()
        WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.LOG_OUT)).click()
        response = WebDriverWait(login, 5).until(EC.text_to_be_present_in_element((By.XPATH, '//main'), 'Вход'))
        assert response == True
        login.quit()

