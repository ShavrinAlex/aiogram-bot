from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
import keyboards
from keyboards.profile.calculator.callback_datas import calc_callback
from loader import dp
from states.calculator import CalculatorState


@dp.callback_query_handler(calc_callback.filter(operation_name='num'), state=CalculatorState.num_2)
async def wait_num_2(call: CallbackQuery, state: FSMContext, callback_data: dict):

    # Записываем число в переменную
    num2 = callback_data.get('meaning')

    # Устанавливаем клавиатуру для получения ответа
    await call.message.edit_reply_markup(keyboards.profile.calculator.calc_operation.get_answer)

    await call.answer(
        text='Чтобы узнать результат, нажмите кнопку "Получить ответ"'
    )

    # Убираем часики
    await call.answer(cache_time=60)

    await state.update_data(num2=num2)
    await CalculatorState.answer.set()
