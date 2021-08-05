from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.profile.calculator.callback_datas import calc_callback
from loader import dp
from states.calculator import CalculatorState


@dp.callback_query_handler(calc_callback.filter(operation_name='operation'), state=CalculatorState.operator)
async def wait_operator(call: CallbackQuery, state: FSMContext, callback_data: dict):

    # Присваиваем команду переменной
    operation = callback_data.get('meaning')

    # Проверяем: не является ли сообщение оператором с выведеной клавиатуры
    if not (operation in ['+', '-', '*', '/']):
        await call.message.reply(
            text='Воспользуйтесь клавиатурой'
        )
        return False

    await call.answer(
        text='Введите второе число'
    )

    # Убираем часики
    await call.answer(cache_time=60)

    await state.update_data(operator=operation)
    await CalculatorState.num_2.set()
