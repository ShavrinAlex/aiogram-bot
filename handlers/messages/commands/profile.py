from aiogram.types import Message
from loader import dp
import keyboards


@dp.message_handler(commands='profile')
async def start(message: Message):
    # Приветствуем и выводим кнопки профиля
    await message.answer(
        text=f'Привет, {message.from_user.full_name}',
        reply_markup=keyboards.profile_operation.keyboard
    )

