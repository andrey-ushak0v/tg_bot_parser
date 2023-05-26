from aiogram.utils.markdown import hlink
from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel

from config import API_HASH, API_ID
from helpers import get_first_sentence, get_first_verb

LIMIT = 20

api_id = API_ID
api_hash = API_HASH
client = TelegramClient(
    'anon',
    api_id,
    api_hash,
    system_version="4.16.30-vxCUSTOM")

client.start()


async def main_func(link):
    if link.isdigit():
        entity = PeerChannel(int(link))
    else:
        entity = link

    channel = await client.get_entity(entity)
    all_posts = await client.get_messages(channel, limit=LIMIT)

    p_list = ''
    p_list += f'{channel.title}\n\n'

    for post in all_posts:
        if hasattr(post.reactions, 'results'):
            res = post.reactions.results
            st_count = 0
            for i in res:
                if i.count > st_count:
                    st_count = i.count
            for j in res:
                if j.count == st_count:
                    p_list += j.reaction.emoticon

        post_message = post.message.replace('\n\n', ' ').replace('\n', ' ')
        post_text = get_first_sentence(post_message)
        verb = get_first_verb(post_text)
        verb_link = hlink(verb, f'https://t.me/{channel.username}/{post.id}')
        post_text_with_link = post_text.replace(verb, verb_link)
        p_list += f'{post_text_with_link}\n\n'
    return p_list
