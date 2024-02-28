from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


def test_from_lk_to_constructor():
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
    driver.find_element(By.XPATH, locators.button_lk).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.exit_button)))
    driver.find_element(By.LINK_TEXT, locators.constructor).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
    assert driver.find_element(By.CLASS_NAME, locators.text_main).text == "Соберите бургер"
    driver.quit()


def test_constructor():
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
    driver.find_element(By.LINK_TEXT, locators.constructor).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, locators.text_main)))
    driver.find_element(By.XPATH, locators.souses).click()
    assert driver.find_element(By.XPATH, locators.souses_test).text == "Соус с шипами Антарианского плоскоходца"
    driver.find_element(By.XPATH, locators.fillings).click()
    assert driver.find_element(By.XPATH, locators.fillings_test).text == "Филе Люминесцентного тетраодонтимформа"
    driver.find_element(By.XPATH, locators.buns).click()
    assert driver.find_element(By.XPATH, locators.buns_test).text == "Краторная булка N-200i"
    driver.quit()

