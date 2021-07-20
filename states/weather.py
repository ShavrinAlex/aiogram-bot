from aiogram.dispatcher.filters.state import StatesGroup, State


class WeatherState(StatesGroup):
    data = State()
    find_out_the_data = State()
