
import asyncio
import random
from config import key
from aiogram import Bot, Dispatcher
from Parser import parser
from aiogram.filters import CommandStart
from aiogram.types import Message


url = "https://www.anekdot.ru/release/anekdot/week/"
list_jokes = parser(url)

bot = Bot(token=key)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello')


async def main():
    await dp.start_polling(bot)
'''
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Hello!\n I am best Bot \n Send my message")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
'''

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')