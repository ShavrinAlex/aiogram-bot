from aiogram.types import Message

import keyboards.cancel.inline_cancel
from loader import dp
from states.weather import WeatherState


@dp.message_handler(commands='weather')
async def weather(message: Message):
    # Предлагаем ввести название города, в котором нужно узнать погоду
    await message.answer(
        text='Напишите город, в котором хотите узнать погоду',
        reply_markup=keyboards.cancel.inline_cancel.keyboard
    )

    await WeatherState.data.set()
