from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import keyboards
from loader import dp
from states.calculator import CalculatorState


@dp.message_handler(state=CalculatorState.num_2)
async def wait_num_2(message: Message, state: FSMContext):
    if not (message.text.isdigit()):
        await message.reply(
            text='Это не число'
        )
        return False

    await message.answer(
        text='Хотите получить ответ?',
        reply_markup=keyboards.calc_operation.get_answer
    )

    await state.update_data(num2=int(message.text))
    await CalculatorState.answer.set()
