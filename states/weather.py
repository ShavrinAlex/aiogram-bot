from aiogram.dispatcher.filters.state import StatesGroup, State


class WeatherState(StatesGroup):
    data = State()
    search = State()
