from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import keyboards
from loader import dp
from states.guessing import GuessingState


@dp.message_handler(text='Угадайка')
async def start(message: Message):
    await message.answer(
        text='Выберите диапазон, в котором я загадаю число',
        reply_markup=keyboards.guessing.keyboard
    )

    await GuessingState.num_range.set()
