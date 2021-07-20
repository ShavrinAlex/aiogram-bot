from aiogram.types import Message
from loader import dp
import keyboards


@dp.message_handler(commands='games')
async def games(message: Message):
    await message.answer(
        text='В какую игру будем играть?',
        reply_markup=keyboards.games.keyboard
    )
