from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.profile.all_operation.callback_datas import profile_callback


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='👤 Информация о профиле', callback_data=profile_callback.new(
                operation_name='personal_area'
            ))
        ],
        [
            InlineKeyboardButton(text='🌤 Погода', callback_data=profile_callback.new(
                operation_name='weather'
            ))
        ],
        [
            InlineKeyboardButton(text='🎮 Игры', callback_data=profile_callback.new(
                operation_name='games'
            ))
        ],
        [
            InlineKeyboardButton(text='⌨ Калькулятор', callback_data=profile_callback.new(
                operation_name='calculator'
            ))
        ]
    ]
)
