from datetime import datetime
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import keyboards
from loader import dp
from states.weather import WeatherState


@dp.message_handler(text='Узнать погоду', state=WeatherState.find_out_the_data)
async def output_data(message: Message, state: FSMContext):
    state_data = await state.get_data()
    data = state_data['weather_data']

    city = data['name']
    country = data['sys']['country']
    sky = data['weather'][0]['description']
    temp = data['main']['temp']
    temp_feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']

    await message.reply(
        f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
        f'Страна: {country}\nГород: {city}\nТемпература: {temp}°C\nОщущается как: {temp_feels_like}°C\n'
        f'Небо: {sky}\nВлажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с',
        reply_markup=keyboards.profile.keyboard
    )

    await state.finish()
