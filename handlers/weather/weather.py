from loader import dp
from aiogram.types import Message
import requests
import datetime
from config import WEATHER_TOKEN

@dp.message_handler(commands='weather')
async def weather(message: Message):
    await message.answer(
        text='Напишите город в котором хотите узнать погоду',
    )

@dp.message_handler()
async def get_weather(message: Message):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={WEATHER_TOKEN}&units=metric'
        )
        data = r.json()

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
    except:
        await message.reply(
            text='Проверьте правильность написания города'
        )