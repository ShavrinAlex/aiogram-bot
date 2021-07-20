from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loader import dp
from states.calculator import CalculatorState


@dp.message_handler(state=CalculatorState.num_1)
async def wait_num_1(message: Message, state: FSMContext):
    if not (message.text.isdigit()):
        await message.reply(
            text='Это не число'
        )
        return False

    await message.answer(
        text='Введите второе число'
    )

    await state.update_data(num1=int(message.text))
    await CalculatorState.num_2.set()
