import asyncio
from bot import Bot
from parse_channel import GetPosts
#from bridge.bridge import start_bridge
import tracemalloc
#import nltk
#import schedule
import config


class DigestApp:
    def __init__(self):

        api_id = config.API_ID
        api_hash = config.API_HASH
        bot_token = config.TOKEN
        phone_bot = config.phone_bot

        self.bot = Bot(
            api_id, api_hash, bot_token)
        self.get_posts = GetPosts(
            api_id, api_hash, phone_bot)

        # nltk.download('averaged_perceptron_tagger')

    def start(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(self.bot.start(
        ), self.get_posts.start(), self.bot.start_handlers()))


if __name__ == '__main__':
    tracemalloc.start()
    app = DigestApp()
    app.start()
