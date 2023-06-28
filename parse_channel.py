from aiogram.utils.markdown import hlink
from telethon.sync import TelegramClient

#from config import API_HASH, API_ID
from helpers import (check_is_dight,
                     get_first_sentence,
                     get_first_verb,
                     save_figure,
                     )


class GetPosts:
    def __init__(self, api_id, api_hash, phone_number):
        self.client = TelegramClient('bot', api_id, api_hash, system_version="4.16.30-vxCUSTOM")
        self.phone_number = phone_number
        self.bridge = None

    async def start(self):
        
        await self.client.connect()
        await self.client.send_code_request(self.phone_number)

        await self.client.run_until_disconnected()

    async def get_posts(self, link):
        entity = check_is_dight(link)
        channel = await self.client.get_entity(entity)
        all_posts = await self.client.get_messages(channel, limit=10)

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



#LIMIT = 10
#
#api_id = API_ID
#api_hash = API_HASH
#client = TelegramClient(
#    'bot',
#    api_id,
#    api_hash,
#    system_version="4.16.30-vxCUSTOM")
#
#client.start()


#async def get_posts(link):
#    entity = check_is_dight(link)
#    channel = await client.get_entity(entity)
#    all_posts = await client.get_messages(channel, limit=LIMIT)
#
#    if not all_posts:
#        return 'в канале пусто'
#
#    p_list = ''
#    p_list += f'{channel.title}\n\n'
#
#    count_list_y = []
#    react_list_x = []
#
#    number_post = 1
#    for post in all_posts:
#
#        if hasattr(post.reactions, 'results'):
#            res = post.reactions.results
#            st_count = 0
#            for i in res:
#                if i.count > st_count:
#                    st_count = i.count
#
#            for j in res:
#                if j.count == st_count:
#                    p_list += j.reaction.emoticon
#                    count_list_y.append(st_count)
#                    react_list_x.append(
#                        f'п{number_post} {j.reaction.emoticon}')
#                    number_post += 1
#                break
#
#        post_message = post.message.replace('\n\n', ' ').replace('\n', ' ')
#        post_text = get_first_sentence(post_message)
#        verb = get_first_verb(post_text)
#        verb_link = hlink(verb, f'https://t.me/{channel.username}/{post.id}')
#        post_text_with_link = post_text.replace(verb, verb_link)
#        p_list += f'{post_text_with_link}\n\n'
#
#    save_figure(react_list_x, count_list_y, channel.title)
#
#    return p_list
#

#@client.on(events.NewMessage(pattern='/start'))
#async def start(event):
#    await event.respond('Пришли ссылку на канал')
#
#
#@client.on(events.NewMessage)
#async def send_posts(event):
#    if check_link(event.raw_text):
#        send_to_user = await get_posts(event.raw_text)
#        ph = open('saved_figure.png', 'rb')
#        await client.send_message(
#            send_to_user, ph)
##            photo=ph,
##            caption=send_to_user,
##            parse_mode='HTML'
##                )
#    
#        print(event.raw_text)
#        await event.respond('отправил')
#
#
#def main():
#    client.run_until_disconnected()
#
#
#if __name__ == '__main__':
#    main()