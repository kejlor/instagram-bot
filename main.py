from bot import Bot
from bot_service import BotService

bot = Bot("YOUR_LOGIN", "YOUR_PASSWORD", "PROFILE_YOU_WANT_TO_DOWNLOAD_PHOTOS")
bot_service = BotService
bot_service.check_if_it_is_profile_or_tag(bot)
bot_service.scroll_down(1, bot)
bot_service.download_images(bot)
