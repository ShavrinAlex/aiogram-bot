import requests
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import keyboards
from config import WEATHER_TOKEN
from loader import dp
from states.weather import WeatherState


@dp.message_handler(state=WeatherState.data)
async def wait_city(message: Message, state: FSMContext):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={WEATHER_TOKEN}&units=metric'
        )

        await state.update_data(data=r.json())
        await WeatherState.seach.set()
        await message.answer(
            text='Чтобы получить данные, нажмите на кнопку "Узнать погоду"',
            reply_markup=keyboards.weather_search.keyboard
        )
    except:
        await message.reply(
            text='Проверьте правильность написания города'
        )
