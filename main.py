import random
#from aiogram.utils import executor
from tok import key
from bs4 import BeautifulSoup
from aiogram import Dispatcher,  Bot, types
from Parser import parser





url = "https://www.anekdot.ru/release/anekdot/week/"
list_jokes = parser(url)
#print(list_jokes)

bot = Bot(key)
dp = Dispatcher()

dp.message_h (commands=['start'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Get anekdot',callback_data="joke"))
    await message.reply('Hello, Here you can get an anecdote')
@dp.message()
async def message_handler(message: types.Message) -> None:
    await SendMessage(chat_id=message.from_user.id, text=message.text)
async def main():
    await dp.start_polling(bot)