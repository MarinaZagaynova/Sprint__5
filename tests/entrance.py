from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


def test_entrance_lk():
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
    assert driver.find_element(By.CLASS_NAME, locators.entrance_button).text == "Оформить заказ"
    driver.quit()


def test_entrance_main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance_button)))
    driver.find_element(By.CLASS_NAME, locators.entrance_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
    driver.find_element(By.XPATH, locators.email_login).send_keys(locators.email_send)
    driver.find_element(By.XPATH, locators.password_registration).send_keys(locators.password_send)
    driver.find_element(By.CLASS_NAME, locators.entrance_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
    assert driver.find_element(By.CLASS_NAME, locators.entrance_button).text == "Оформить заказ"
    driver.quit()


def test_entrance_registration():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.button_lk)))
    driver.find_element(By.XPATH, locators.button_lk).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
    driver.find_element(By.LINK_TEXT, locators.registration).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
    driver.find_element(By.CLASS_NAME, locators.entrance_link).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
    driver.find_element(By.XPATH, locators.email_login).send_keys(locators.email_send)
    driver.find_element(By.XPATH, locators.password_registration).send_keys(locators.password_send)
    driver.find_element(By.CLASS_NAME, locators.entrance_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
    assert driver.find_element(By.CLASS_NAME, locators.entrance_button).text == "Оформить заказ"
    driver.quit()


def test_entrance_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.button_lk)))
    driver.find_element(By.XPATH, locators.button_lk).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
    driver.find_element(By.LINK_TEXT, locators.restore_password).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
    driver.find_element(By.CLASS_NAME, locators.entrance_link).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.entrance)))
    driver.find_element(By.XPATH, locators.email_login).send_keys(locators.email_send)
    driver.find_element(By.XPATH, locators.password_registration).send_keys(locators.password_send)
    driver.find_element(By.CLASS_NAME, locators.entrance_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
    assert driver.find_element(By.CLASS_NAME, locators.entrance_button).text == "Оформить заказ"
    driver.quit()

