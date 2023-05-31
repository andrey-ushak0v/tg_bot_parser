from aiogram.utils.markdown import hlink
from telethon.sync import TelegramClient

from config import API_HASH, API_ID
from helpers import (check_is_dight,
                     get_first_sentence,
                     get_first_verb,
                     save_figure)

LIMIT = 10

api_id = API_ID
api_hash = API_HASH
client = TelegramClient(
    'anon',
    api_id,
    api_hash,
    system_version="4.16.30-vxCUSTOM")

client.start()


async def main_func(link):
    entity = check_is_dight(link)
    channel = await client.get_entity(entity)
    all_posts = await client.get_messages(channel, limit=LIMIT)

    if not all_posts:
        return 'в канале пусто'

    p_list = ''
    p_list += f'{channel.title}\n\n'

    count_list_y = []
    react_list_x = []

    number_post = 1
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
                    count_list_y.append(st_count)
                    react_list_x.append(
                        f'п{number_post} {j.reaction.emoticon}')
                    number_post += 1
                break

        post_message = post.message.replace('\n\n', ' ').replace('\n', ' ')
        post_text = get_first_sentence(post_message)
        verb = get_first_verb(post_text)
        verb_link = hlink(verb, f'https://t.me/{channel.username}/{post.id}')
        post_text_with_link = post_text.replace(verb, verb_link)
        p_list += f'{post_text_with_link}\n\n'

    save_figure(react_list_x, count_list_y, channel.title)

    return p_list
