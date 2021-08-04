from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.cancel.callback_datas import cancel_callback
from keyboards.games.inline.callback_datas import game_callback


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='128', callback_data=game_callback.new(
                type_game='guessing', range='128'
            )),
            InlineKeyboardButton(text='256', callback_data=game_callback.new(
                type_game='guessing', range='256'
            ))
        ],
        [
            InlineKeyboardButton(text='512', callback_data=game_callback.new(
                type_game='guessing', range='512'
            )),
            InlineKeyboardButton(text='1024', callback_data=game_callback.new(
                type_game='guessing', range='1024'
            ))
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data=cancel_callback.new(
                operation_name='cancel'
            ))
        ]
    ]
)
