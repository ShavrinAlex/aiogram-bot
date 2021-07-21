from aiogram.types import Message
import keyboards.games
from loader import dp


@dp.message_handler(commands='games')
async def games(message: Message):
    await message.answer(
        text='Выберите тип игр',
        reply_markup=keyboards.games.keyboard
    )
