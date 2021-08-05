from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.profile.calculator.callback_datas import calc_callback
from loader import dp
from states.calculator import CalculatorState


@dp.callback_query_handler(calc_callback.filter(operation_name='num'), state=CalculatorState.num_1)
async def wait_num_1(call: CallbackQuery, state: FSMContext, callback_data: dict):

    # Записываем число в переменную
    num1 = callback_data.get('meaning')

    await call.answer(
        text='Введите оператор'
    )

    # Убираем часики
    await call.answer(cache_time=60)

    await state.update_data(num1=num1)
    await CalculatorState.operator.set()
