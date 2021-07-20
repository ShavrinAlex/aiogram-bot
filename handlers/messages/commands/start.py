from aiogram.types import Message
from loader import dp
import keyboards


@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer(
        text=f'Привет, {message.from_user.full_name}',
        reply_markup=keyboards.profile.keyboard
    )

