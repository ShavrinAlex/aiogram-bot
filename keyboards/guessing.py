from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='128'),
            KeyboardButton(text='256')
        ],
        [
            KeyboardButton(text='512'),
            KeyboardButton(text='1024')
        ]
    ]
)