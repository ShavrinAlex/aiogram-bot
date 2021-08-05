from aiogram.types import CallbackQuery
from keyboards.profile.all_operation.callback_datas import profile_callback
from loader import dp
import keyboards
from states.calculator import CalculatorState


@dp.callback_query_handler(profile_callback.filter(operation_name='calculator'))
async def calc(call: CallbackQuery):
    # Выводи клавиатуру и просим указать оператор
    await call.message.answer(
        text='Калькулятор',
        reply_markup=keyboards.profile.calculator.calc_operation.keyboard
    )

    await call.answer(
        text='Введите первое число'
    )

    await CalculatorState.num_1.set()
