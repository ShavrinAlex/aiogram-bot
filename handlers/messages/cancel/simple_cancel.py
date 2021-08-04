from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp


@dp.message_handler(text='Отмена', state='*')
async def cancel(message: Message, state: FSMContext):
    await message.answer(
        text='Вы перемещены в главное меню',
        reply_markup=ReplyKeyboardRemove()
    )

    await state.finish()
