from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.cancel.callback_datas import cancel_callback
from keyboards.profile.calculator.callback_datas import calc_callback


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data=calc_callback.new(
                operation_name='num', meaning=1
            )),
            InlineKeyboardButton(text='2', callback_data=calc_callback.new(
                operation_name='num', meaning=2
            )),
            InlineKeyboardButton(text='3', callback_data=calc_callback.new(
                operation_name='num', meaning=3
            )),
            InlineKeyboardButton(text='+', callback_data=calc_callback.new(
                operation_name='operation', meaning='+'
            ))
        ],
        [
            InlineKeyboardButton(text='4', callback_data=calc_callback.new(
                operation_name='num', meaning=4
            )),
            InlineKeyboardButton(text='5', callback_data=calc_callback.new(
                operation_name='num', meaning=5
            )),
            InlineKeyboardButton(text='6', callback_data=calc_callback.new(
                operation_name='num', meaning=6
            )),
            InlineKeyboardButton(text='-', callback_data=calc_callback.new(
                operation_name='operation', meaning='-'
            ))
        ],
        [
            InlineKeyboardButton(text='7', callback_data=calc_callback.new(
                operation_name='num', meaning=7
            )),
            InlineKeyboardButton(text='8', callback_data=calc_callback.new(
                operation_name='num', meaning=8
            )),
            InlineKeyboardButton(text='9', callback_data=calc_callback.new(
                operation_name='num', meaning=9
            )),
            InlineKeyboardButton(text='*', callback_data=calc_callback.new(
                operation_name='operation', meaning='*'
            ))
        ],
        [
            InlineKeyboardButton(text='0', callback_data=calc_callback.new(
                operation_name='num', meaning=0
            )),
            InlineKeyboardButton(text='/', callback_data=calc_callback.new(
                operation_name='operation', meaning='/'
            ))
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data=cancel_callback.new(
                operation_name='cancel'
            ))
        ]
    ]
)

get_answer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Получить ответ', callback_data=calc_callback.new(
            operation_name='answer', meaning='='
            ))
        ]
    ]
)
