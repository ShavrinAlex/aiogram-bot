from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.profile.calculator.callback_datas import calc_callback
from loader import dp
from states.calculator import CalculatorState


@dp.callback_query_handler(calc_callback.filter(operation_name='answer'), state=CalculatorState.answer)
async def get_answer(call: CallbackQuery, state: FSMContext):

    # Записываем все переменные
    state_data = await state.get_data()
    num_1 = state_data['num1']
    num_2 = state_data['num2']
    operator = state_data['operator']
    answer = eval(f'{num_1} {operator} {num_2}')

    # Выводим ответ
    await call.message.answer(
        text=f'{num_1} {operator} {num_2} = {answer}'
    )

    # Убираем часики и кнопку
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup()

    await state.finish()
