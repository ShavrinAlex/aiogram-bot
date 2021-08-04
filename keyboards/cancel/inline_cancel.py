from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.cancel.callback_datas import cancel_callback


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Отмена', callback_data=cancel_callback.new(
                operation_name='cancel'
            ))
        ]
    ]
)
