from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import (
    ReplyKeyboardBuilder,
    InlineKeyboardBuilder)
from config import cars


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Get anecdot")],
        [KeyboardButton(text="Katalog"), KeyboardButton(text="finish")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Bocno",
)


settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="YouTub",
                              url="https://youtube.com/@sudoteach")]
    ]
)


async def inline_cars():

    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car))
    return keyboard.adjust(2).as_markup()
