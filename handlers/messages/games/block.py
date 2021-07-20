from aiogram.types import Message
from loader import dp


@dp.message_handler(text='Бросить кубик')
async def block(message: Message):
    await message.answer_dice(
        emoji='🎲'
    )
