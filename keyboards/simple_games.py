from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Бросить кубик')
        ],
        [
            KeyboardButton(text='Бросить дротик')
        ]
    ]
)