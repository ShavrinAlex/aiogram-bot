from aiogram.types import Message
import keyboards.games
from loader import dp


@dp.message_handler(commands='games')
async def games(message: Message):
    # Просим выбрать тип игры с выведеной клавиатуры
    await message.answer(
        text='Выберите тип игр:',
        reply_markup=keyboards.games.inline.games.keyboard
    )
