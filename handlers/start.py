import keyboards
from loader import dp
from aiogram.types import Message

@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer(
        text=f'Hello, {message.from_user.full_name}',
        reply_markup=keyboards.main.keyboard
    )
