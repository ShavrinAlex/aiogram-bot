from aiogram.types import Message
from loader import dp


@dp.message_handler(text='Бросить дротик')
async def darts(message: Message):
    await message.answer_dice(
        emoji='🎯'
    )
