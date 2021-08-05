from aiogram.types import CallbackQuery
import keyboards.cancel.inline_cancel
from keyboards.profile.all_operation.callback_datas import profile_callback
from loader import dp
from states.weather import WeatherState


@dp.callback_query_handler(profile_callback.filter(operation_name='weather'))
async def weather(call: CallbackQuery):
    # Убираем часики
    await call.answer(cache_time=60)

    # Предлагаем ввести название города, в котором нужно узнать погоду
    await call.message.answer(
        text='Напишите город, в котором хотите узнать погоду',
        reply_markup=keyboards.cancel.inline_cancel.keyboard
    )

    await WeatherState.data.set()
