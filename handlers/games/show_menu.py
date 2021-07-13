import keyboards
from aiogram.types import Message
from loader import dp


@dp.message_handler(commands='games')
async def games(message: Message):
    await message.answer(
        text='Во что играем?',
        reply_markup=keyboards.games.keyboard
    )
