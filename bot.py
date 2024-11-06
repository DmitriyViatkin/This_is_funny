
import asyncio
from config import key, url
from aiogram import Bot, Dispatcher
from Parser import parser
from app.handlers import router


list_jokes = parser(url)

bot = Bot(token=key)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
