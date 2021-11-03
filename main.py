import os
import time

import wget as wget
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PATH = "YOUR_PATH_TO_WEBDRIVERS"
driver = webdriver.Chrome(PATH)

# open the webpage
driver.get("http://www.instagram.com/")

# target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# enter username and password
username.clear()
username.send_keys("INPUT_YOU_LOGIN")
password.clear()
password.send_keys("INPUT_YOUR_PASSWORD")

time.sleep(5)
alert = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Akceptuję wszystko")]'))).click()

# target the login button and click it
time.sleep(5)
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(7)
alert = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Nie teraz")]'))).click()
time.sleep(7)
alert2 = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Nie teraz")]'))).click()


# We are logged in!

# target the search input field
# time.sleep(5)
# searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Szukaj']")))
# searchbox.clear()

# search for the hashtag cat
# keyword = "milkgore"
# searchbox.send_keys(keyword)
# searchbox.send_keys(Keys.RETURN)

# FIXING THE DOUBLE ENTER
# time.sleep(5)  # Wait for 5 seconds
# my_link = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[0:] + "/')]")))
# my_link.click()

keyword = "juliamajch"

time.sleep(5)
driver.get(f"http://www.instagram.com/{keyword}/")

#scroll down 2 times
#increase the range to sroll more
time.sleep(5)
n_scrolls = 0
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

# target all the link elements on the page
anchors = driver.find_elements_by_tag_name('a')
anchors = [a.get_attribute('href') for a in anchors]
# narrow down all links to image links only
anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

print('Found ' + str(len(anchors)) + ' links to images')
anchors[:5]

images = []

# follow each image link and extract only image at index=1
for a in anchors:
    driver.get(a)
    time.sleep(5)
    img = driver.find_elements_by_tag_name('img')
    img = [i.get_attribute('src') for i in img]
    images.append(img[1])

images[:5]


path = "D:/InstagramBot"
path = os.path.join(path, keyword[0:] + "s")

# create the directory
os.mkdir(path)

path

counter = 0
for image in images:
    save_as = os.path.join(path, keyword[0:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
