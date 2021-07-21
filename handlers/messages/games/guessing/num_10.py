from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import keyboards.profile
from loader import dp
from states.guessing import GuessingState
from .comparison import more_or_less_or_equal


@dp.message_handler(state=GuessingState.num_10)
async def num_10(message: Message, state: FSMContext):
    my_num = (await state.get_data())['my_num']
    attempt = (await state.get_data())['attempt']
    if not (message.text.isdigit()):
        await message.reply(
            text='Это не число'
        )
        return False

    if attempt == 10:
        if more_or_less_or_equal(int(message.text), my_num) != 'Ура! Ты угадал моё число':
            await message.answer(
                text=f'Ничего страшного, тебе обязательно повезет в другой раз!\n'
                     f"A загаданное мной число было: {(await state.get_data())['my_num']}",
                reply_markup=keyboards.profile.keyboard
            )
            await state.finish()
        else:
            await message.answer(
                text=f'{more_or_less_or_equal(int(message.text), my_num)}',
                reply_markup=keyboards.profile.keyboard
            )
            await state.finish()
