import os
import time

import selenium
import wget as wget
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:/Users/Kejlor/PycharmProjects/chromedriver.exe"
SAVE_PATH = "D:/InstagramBot"


class Bot:

    def __init__(self, login, password, keyword):
        self.login = login
        self.keyword = keyword
        self.driver = webdriver.Chrome(PATH)
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
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Akceptuję wszystko")]'))).click()

        time.sleep(5)
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

        time.sleep(7)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Nie teraz")]'))).click()
        time.sleep(7)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Nie teraz")]'))).click()

    def open_profile(self):
        time.sleep(5)
        self.driver.get(f"http://www.instagram.com/{self.keyword}/")

    def open_explore_tags(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/explore/tags/{self.keyword[1:]}/")

    def check_what_to_open(self):
        time.sleep(5)
        if self.keyword[0] != '#':
            self.open_profile()
        else:
            self.open_explore_tags()

    def scroll_down(self, n_scrolls):
        time.sleep(5)
        for j in range(0, int(n_scrolls)):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

    def download_images(self):
        anchors = self.driver.find_elements_by_tag_name('a')
        anchors = [a.get_attribute('href') for a in anchors]
        anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

        print('Found ' + str(len(anchors)) + ' links to images')
        anchors[:5]

        images = []

        for a in anchors:
            self.driver.get(a)
            time.sleep(5)
            img = self.driver.find_elements_by_tag_name('img')
            img = [i.get_attribute('src') for i in img]
            images.append(img[1])

        images[:5]

        path = SAVE_PATH
        if self.keyword[0] == '#':
            path = os.path.join(path, self.keyword[1:] + "s")
        else:
            path = os.path.join(path, self.keyword[0:] + "s")

        os.mkdir(path)

        path

        counter = 0
        for image in images:
            if self.keyword[0] == '#':
                save_as = os.path.join(path, self.keyword[1:] + str(counter) + '.jpg')
            else:
                save_as = os.path.join(path, self.keyword[0:] + str(counter) + '.jpg')
            wget.download(image, save_as)
            counter += 1

    def get_first_post(self):
        self.driver.find_element_by_class_name("eLAPa").click()
        time.sleep(3)

    def nested_check(self):
        try:
            time.sleep(1)
            nes_nex = self.driver.find_element_by_class_name("    coreSpriteRightChevron  ")
            return nes_nex

        except selenium.common.exceptions.NoSuchElementException:
            return 0

    def next_post(self):
        try:
            nex = self.driver.find_element_by_class_name("QBdPU ")
            return nex
        except selenium.common.exceptions.NoSuchElementException:
            return 0
