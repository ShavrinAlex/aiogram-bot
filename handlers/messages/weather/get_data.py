import requests
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import keyboards
from config import WEATHER_TOKEN
from loader import dp
from states.weather import WeatherState


@dp.message_handler(state=WeatherState.data)
async def get_data(message: Message, state: FSMContext):
    r = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={WEATHER_TOKEN}&units=metric'
    )

    weather_data = r.json()

    if not ('message' in weather_data):
        await state.update_data(weather_data=weather_data)
        await WeatherState.find_out_the_data.set()
        await message.answer(
            text='Чтобы получить данные, нажмите на кнопку "Узнать погоду"',
            reply_markup=keyboards.weather_operation.keyboard
        )

    await message.reply(
        text='Проверьте правильность написания названия города'
    )
