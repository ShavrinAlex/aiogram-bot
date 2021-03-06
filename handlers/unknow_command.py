from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import keyboards
from loader import dp


@dp.message_handler(state='*')
async def message_answer(message: Message, state: FSMContext):
    await message.answer(
        text='Неизвестная комманда'
    )

    await state.finish()
