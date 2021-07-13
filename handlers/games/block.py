from aiogram.types import Message
from loader import dp

@dp.message_handler(text='Кинуть кубик')
async def throw_block(message: Message):
    await message.answer_dice(
        emoji='🎲'
    )
