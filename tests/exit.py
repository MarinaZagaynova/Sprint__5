from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


def test_exit():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.button_lk)))
    driver.find_element(By.XPATH, locators.button_lk).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
    driver.find_element(By.XPATH, locators.email_login).send_keys(locators.email_send)
    driver.find_element(By.XPATH, locators.password_registration).send_keys(locators.password_send)
    driver.find_element(By.CLASS_NAME, locators.entrance_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
    driver.find_element(By.XPATH, locators.button_lk).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.exit_button)))
    driver.find_element(By.CLASS_NAME, locators.exit_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.LINK_TEXT, locators.registration)))
    assert driver.find_element(By.CLASS_NAME, locators.entrance_button).text == "Войти"
    driver.quit()
