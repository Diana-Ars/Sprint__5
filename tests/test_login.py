from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import generate_registration_data
from locators import Locators
from curl import *

class TestLogin:

    def test_login_from_main_page_by_log_in_account(self, registration):
        registration.get(main_site)
        email, password = generate_registration_data()
        WebDriverWait(registration, 5).until(EC.element_to_be_clickable(Locators.ENTER_TO_ACC)).click()
        registration.find_element(*Locators.EMAIL).send_keys(email)
        registration.find_element(*Locators.PASSWORD).send_keys(password)
        WebDriverWait(registration, 5).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON)).click()
        current_url = registration.current_url
        assert current_url == main_site + 'login'


    def test_login_by_personal_acc(self, registration):
        registration.get(main_site)
        email, password = generate_registration_data()
        WebDriverWait(registration, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON)).click()
        registration.find_element(*Locators.EMAIL).send_keys(email)
        registration.find_element(*Locators.PASSWORD).send_keys(password)
        WebDriverWait(registration, 5).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON)).click()
        current_url = registration.current_url
        assert current_url == main_site + 'login'


    def test_login_from_registration_form(self, registration):
        registration.get(main_site)
        WebDriverWait(registration, 5).until(EC.element_to_be_clickable(Locators.ENTER_TO_ACC)).click()
        WebDriverWait(registration, 5).until(EC.element_to_be_clickable(Locators.REG_BUTTON)).click()
        WebDriverWait(registration, 5).until(EC.element_to_be_clickable(Locators.ENTER_IN_REG_FORM)).click()
        email, password = generate_registration_data()
        registration.find_element(*Locators.EMAIL).send_keys(email)
        registration.find_element(*Locators.PASSWORD).send_keys(password)
        WebDriverWait(registration, 5).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON)).click()
        current_url = registration.current_url
        assert current_url == main_site + 'login'


    def test_login_from_recover_password(self, registration):
        registration.get(main_site)
        WebDriverWait(registration, 7).until(EC.element_to_be_clickable(Locators.ENTER_TO_ACC)).click()
        WebDriverWait(registration, 7).until(EC.element_to_be_clickable(Locators.RECOVER_PASSWORD)).click()
        WebDriverWait(registration, 7).until(EC.element_to_be_clickable(Locators.ENTER_IN_REG_FORM)).click()
        email, password = generate_registration_data()
        registration.find_element(*Locators.EMAIL).send_keys(email)
        registration.find_element(*Locators.PASSWORD).send_keys(password)
        WebDriverWait(registration, 7).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON)).click()
        current_url = registration.current_url
        assert current_url == main_site + 'login'


