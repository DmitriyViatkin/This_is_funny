
import asyncio
from config import key
from aiogram import Bot, Dispatcher, F
from Parser import parser
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


url = "https://www.anekdot.ru/release/anekdot/week/"
list_jokes = parser(url)

bot = Bot(token=key)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Hello.\nYou_ID: {message.from_user.id}\nName:{message.from_user.first_name}')


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('It is command /help')


@dp.message(F.text == "How are You?")
async def how_are_you(message: Message):
    await message.answer('Good')


@dp.message(F.text == 'Arestovich')
async def aristovich(message: Message):
    await message.answer('Trol')


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
