import os
import time

import wget


class BotService:
    @staticmethod
    def open_profile(bot) -> None:
        time.sleep(5)
        bot.driver.get(f"http://www.instagram.com/{bot.keyword}/")

    @staticmethod
    def open_explore_tags(bot) -> None:
        time.sleep(5)
        bot.driver.get(f"https://www.instagram.com/explore/tags/{bot.keyword[1:]}/")

    @staticmethod
    def check_if_it_is_profile_or_tag(bot) -> None:
        time.sleep(5)
        if bot.keyword[0] != '#':
            BotService.open_profile(bot)
        else:
            BotService.open_explore_tags(bot)

    @staticmethod
    def scroll_down(n_scrolls, bot) -> None:
        time.sleep(5)
        for j in range(0, int(n_scrolls)):
            bot.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

    @staticmethod
    def download_images(bot) -> None:
        anchors = bot.driver.find_elements_by_tag_name('a')
        anchors = [a.get_attribute('href') for a in anchors]
        anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

        print('Found ' + str(len(anchors)) + ' links to images')
        anchors[:5]

        images = []

        for a in anchors:
            bot.driver.get(a)
            time.sleep(5)
            img = bot.driver.find_elements_by_tag_name('img')
            img = [i.get_attribute('src') for i in img]
            images.append(img[1])

        images[:5]

        path = bot.SAVE_PATH
        if bot.keyword[0] == '#':
            path = os.path.join(path, bot.keyword[1:] + "s")
        else:
            path = os.path.join(path, bot.keyword[0:] + "s")

        os.mkdir(path)

        path

        counter = 0
        for image in images:
            if bot.keyword[0] == '#':
                save_as = os.path.join(path, bot.keyword[1:] + str(counter) + '.jpg')
            else:
                save_as = os.path.join(path, bot.keyword[0:] + str(counter) + '.jpg')
            wget.download(image, save_as)
            counter += 1

    @staticmethod
    def open_first_post(bot):
        bot.driver.find_element_by_class_name("eLAPa").click()
        time.sleep(3)
