import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Bot:
    PATH = "YOUR_PATH_FOR_WEBDRIVERS"
    SAVE_PATH = "DESIRED_PATH_TO_SAVE_FILES"

    def __init__(self, login, password, keyword):
        self.login = login
        self.keyword = keyword
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("http://www.instagram.com/")
        username_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

        username_field.clear()
        username_field.send_keys(login)
        password_field.clear()
        password_field.send_keys(password)

        time.sleep(5)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept all")]'))).click()

        time.sleep(5)
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

        time.sleep(7)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not now")]'))).click()
        time.sleep(7)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not now")]'))).click()
