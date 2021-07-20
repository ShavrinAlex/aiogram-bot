from datetime import datetime
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loader import dp
from states.weather import WeatherState


@dp.message_handler(text='Узнать погоду', state=WeatherState.search)
async def get_data(message: Message, state: FSMContext):
    state_data = await state.get_data()
    data = state_data('data')

    city = data['name']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']

    await message.reply(
        f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
        f'Погода в городе: {city}\nТемпература: {temp}°C\n'
        f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с'
    )

    await state.finish()
