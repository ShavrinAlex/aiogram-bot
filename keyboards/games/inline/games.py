from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.cancel.callback_datas import cancel_callback
from keyboards.games.inline.callback_datas import game_callback

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Простые игры', callback_data=game_callback.new(
                type_game='simple_games', range='0'
            )),
            InlineKeyboardButton(text='Угадайка', callback_data=game_callback.new(
                type_game='guessing', range='0'
            ))
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data=cancel_callback.new(
                operation_name='cancel'
            ))
        ]
    ]
)
