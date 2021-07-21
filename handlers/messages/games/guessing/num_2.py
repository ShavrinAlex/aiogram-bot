from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import keyboards
from loader import dp
from states.guessing import GuessingState
from .comparison import more_or_less_or_equal


@dp.message_handler(state=GuessingState.num_2)
async def num_2(message: Message, state: FSMContext):
    my_num = (await state.get_data())['my_num']

    if not (message.text.isdigit()):
        await message.reply(
            text='Это не число'
        )
        return False

    if more_or_less_or_equal(int(message.text), my_num) == 'Ура! Ты угадал моё число':
        await message.answer(
            text=f"{more_or_less_or_equal(int(message.text), my_num)}",
            reply_markup=keyboards.profile.keyboard
        )
        await state.finish()
    else:
        await message.answer(
            text=f'{more_or_less_or_equal(int(message.text), my_num)}'
        )
        await GuessingState.num_3.set()
