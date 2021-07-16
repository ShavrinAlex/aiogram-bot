from aiogram.types import Message
from loader import dp
import keyboards
from states.calculator import CalculatorState


@dp.message_handler(commands='calc')
async def calc(message: Message):
    await message.answer(
        text='Введите оператор',
        reply_markup=keyboards.calc_operation.keyboard
    )
    await CalculatorState.operator.set()
