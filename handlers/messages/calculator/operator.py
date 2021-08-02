from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loader import dp
from states.calculator import CalculatorState


@dp.message_handler(state=CalculatorState.operator)
async def wait_operator(message: Message, state: FSMContext):
    # Проверяем: не является ли сообщение оператором с выведеной клавиатуры
    if not (message.text in ['+', '-', '*', '/']):
        await message.reply(
            text='Воспользуйтесь клавиатурой'
        )
        return False

    await message.answer(
        text='Введите первое число'
    )

    await state.update_data(operator=message.text)
    await CalculatorState.num_1.set()
