#from aiogram import Bot, Dispatcher, executor, types
from telethon.sync import TelegramClient, events
import config
from helpers import check_link
from parse_channel import GetPosts


class Bot:
    def __init__(self, api_id, api_hash, bot_token):
        self.client = TelegramClient(
            'bot_send_msg', api_id, api_hash).start(bot_token=config.TOKEN)

        self.bridge = None

    async def start(self):
        await self.client.run_until_disconnected()

    async def start_handlers(self):
        self.client.add_event_handler(
            self.handle_start,
            events.NewMessage(pattern='/start')
            )

    async def handle_start(self, event):
       await self.client.send_message(event.sender_id, message='qq')

    async def send_posts(self, event):
        user_id = event.sender_id
        if check_link(event.raw_txt):
            send_to_user = await GetPosts.get_posts(event.raw_txt)
            ph = open('saved_figure.png', 'rb')
            await self.client.send_message(user_id, ph, send_to_user, parse_mode='HTML')



