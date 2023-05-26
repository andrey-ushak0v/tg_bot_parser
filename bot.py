from aiogram import Bot, Dispatcher, executor, types

import config
from helpers import check_link
from parse_channel import main_func

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('дай ссылку')


@dp.message_handler()
async def send_posts(message: types.Message):
    if check_link(message.text):
        send_to_user = await main_func(message.text)
        await message.answer(text=send_to_user, parse_mode='HTML')


if __name__ == '__main__':
    executor.start_polling(dp)
