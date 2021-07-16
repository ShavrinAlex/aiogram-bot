from aiogram.dispatcher.filters.state import StatesGroup, State

class CalculatorState(StatesGroup):
    operator = State()
    num_1 = State()
    num_2 = State()
    answer = State()
