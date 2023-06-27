
from bot import Bot
from parse_channel import GetPosts

import asyncio
from telethon.tl.types import PeerChannel


class Bridge:
    def __init__(self, get_posts: GetPosts, bot: Bot):
        self.phone_bot: GetPosts = get_posts
        self.token_bot: Bot = bot

