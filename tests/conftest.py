import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers import generate_registration_data
from curl import *
from data import Fixed
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    options = Options()
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

@pytest.fixture()
def registration(driver):
    driver.find_element(*Locators.ENTER_TO_ACC).click()
    email, password = generate_registration_data()
    driver.find_element(*Locators.REG_BUTTON).click()
    driver.find_element(*Locators.NAME).send_keys(email)
    driver.find_element(*Locators.EMAIL).send_keys(email)
    driver.find_element(*Locators.PASSWORD).send_keys(password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    yield driver


@pytest.fixture()
def login(driver):
    driver.find_element(*Locators.ENTER_TO_ACC).click()
    email, password = generate_registration_data()
    driver.find_element(*Locators.REG_BUTTON).click()
    driver.find_element(*Locators.NAME).send_keys(email)
    driver.find_element(*Locators.EMAIL).send_keys(email)
    driver.find_element(*Locators.PASSWORD).send_keys(password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    driver.get(main_site)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ENTER_TO_ACC)).click()
    driver.find_element(*Locators.EMAIL).send_keys(email)
    driver.find_element(*Locators.PASSWORD).send_keys(password)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON)).click()

    yield driver


