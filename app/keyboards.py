from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Get anecdot')],
    [KeyboardButton(text='Katalog'), KeyboardButton(text='finish')]
    ])
