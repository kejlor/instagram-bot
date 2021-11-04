from bot import Bot

bot = Bot("YOUR_LOGIN", "YOUR_PASSWORD", "PROFILE_YOU_WANT_TO_DOWNLOAD_PHOTOS")
bot.open_profile()
bot.scroll_down(0)
bot.download_images()
