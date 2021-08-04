from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.profile.inline.callback_datas import profile_callback


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Информация о профиле', callback_data=profile_callback.new(
                operation_name='personal_area'
            ))
        ]
    ]
)
