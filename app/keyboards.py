from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from config import cars


main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Catalog', callback_data='catalog')],
        [InlineKeyboardButton(text="Contact", callback_data='Contact'),
         InlineKeyboardButton(text='Korzina', callback_data='Bug')]
    ])


settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="YouTub", url="https://youtube.com/\
                              @sudoteach")]
    ]
)


async def inline_cars():

    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(
            InlineKeyboardButton(
                text=car,
                url="https://drive.google.com/file/\
                    d/1qWvxFqub7IwJP4UAMIzB8wDXQ5WZYGxm/view?usp=drive_link",
            )
        )
    return keyboard.adjust(2).as_markup()
