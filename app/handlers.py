from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        f"Hello.\nYou_ID: {message.from_user.id}\
                        \nName:{message.from_user.first_name}",
        reply_markup=kb.main
    )


@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("It is command /help")


@router.message(F.text == "How are You?")
async def how_are_you(message: Message):
    await message.answer("Good")


@router.message(F.text == "Arestovich")
async def aristovich(message: Message):
    await message.answer("Trol")
