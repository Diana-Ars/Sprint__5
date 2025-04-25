from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from curl import *
from helpers import generate_registration_data
from locators import Locators
from data import *

class TestSuccessRegistration:

    def test_successful_registration_by_new_data(self, driver):
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.ENTER_TO_ACC)).click()
        email, password = generate_registration_data()
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.REG_BUTTON)).click()
        driver.find_element(*Locators.NAME).send_keys(email)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
        current_url = driver.current_url
        assert current_url == main_site + 'register'
        driver.quit()

class TestFailedRegistration:

    def test_failed_registration_by_password_less_6_symbols(self, driver):
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.ENTER_TO_ACC)).click()
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.REG_BUTTON)).click()
        driver.find_element(*Locators.NAME).send_keys(Fixed.name)
        driver.find_element(*Locators.EMAIL).send_keys(Fixed.email)
        driver.find_element(*Locators.PASSWORD).send_keys('12345') #ввод пароля менее 6 символов - 5 символов
        current_url = driver.current_url
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
        error_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators. ERROR_MESSAGE_PASSWORD)).text
        assert error_text == 'Некорректный пароль'
        assert driver.current_url == current_url
        driver.quit()

    def test_failed_registration_by_empty_name(self, driver):
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.ENTER_TO_ACC)).click()
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.REG_BUTTON)).click()
        driver.find_element(*Locators.NAME).send_keys('') # ввод пустого значения в поле name
        driver.find_element(*Locators.EMAIL).send_keys(Fixed.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Fixed.password)
        current_url = driver.current_url
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
        assert driver.current_url == current_url
        driver.quit()

    def test_failed_registration_by_email_without_at_sign(self, driver):
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.ENTER_TO_ACC)).click()
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.REG_BUTTON)).click()
        driver.find_element(*Locators.NAME).send_keys(Fixed.name)
        driver.find_element(*Locators.EMAIL).send_keys('dianaarslanova20126ya.ru') # ввод в поле email значения без символа @
        driver.find_element(*Locators.PASSWORD).send_keys(Fixed.password)
        current_url = driver.current_url
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
        assert driver.current_url == current_url
        driver.quit()