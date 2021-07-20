from aiogram.types import Message
from loader import dp
from states.weather import WeatherState


@dp.message_handler(commands='weather')
async def weather(message: Message):
    await message.answer(
        text='Напишите город, в котором хотите узнать погоду',
    )

    await WeatherState.data.set()
