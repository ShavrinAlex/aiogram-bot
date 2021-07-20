from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import keyboards
from loader import dp
from states.calculator import CalculatorState


@dp.message_handler(text='Получить ответ', state=CalculatorState.answer)
async def get_answer(message: Message, state: FSMContext):
    state_data = await state.get_data()
    num_1 = state_data['num1']
    num_2 = state_data['num2']
    operator = state_data['operator']
    answer = eval(f'{num_1} {operator} {num_2}')

    await message.answer(
        text=f'{num_1} {operator} {num_2} = {answer}',
        reply_markup=keyboards.main.keyboard
    )

    await state.finish()
