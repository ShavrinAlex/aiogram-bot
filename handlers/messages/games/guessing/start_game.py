from aiogram.types import Message
import keyboards
from loader import dp
from states.guessing import GuessingState


@dp.message_handler(text='Угадайка')
async def start(message: Message):
    # Предлагает выбрать диапазон чисел для загадывания из выведеной клавиатуры
    await message.answer(
        text='Выберите диапазон, в котором я загадаю число',
        reply_markup=keyboards.games.guessing.keyboard,
    )

    await GuessingState.num_range.set()
