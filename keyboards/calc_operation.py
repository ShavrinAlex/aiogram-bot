from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        keyboard=[
        [
            KeyboardButton(text='+'),
            KeyboardButton(text='-')
        ],
        [
            KeyboardButton(text='*'),
            KeyboardButton(text='/')
        ]
    ]
)

get_answer = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Получить ответ')
        ]
    ]
)


