from math import log2
from random import randint
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
import keyboards
from keyboards.profile.games.inline.callback_datas import game_callback
from loader import dp
from states.guessing import GuessingState


@dp.callback_query_handler(game_callback.filter(type_game='guessing'), state=GuessingState.num_range)
async def set_range(call: CallbackQuery, state: FSMContext, callback_data: dict):
    # Убираем часики
    await call.answer(cache_time=60)

    # Присваиваем выбранный диапазон переменной
    num_range = int(callback_data.get('range'))

    # Сохранение выбранного диапазона и кол-ва попыток
    await state.update_data(num_range=num_range)
    await state.update_data(attempt=int(log2((await state.get_data())['num_range'])))

    # Уведомление о кол-ве попыток
    await call.message.answer(
        text=f"У вас есть {int((await state.get_data())['attempt'])} попыток, чтобы отгадать загаданное мной число",
        reply_markup=keyboards.cancel.inline_cancel.keyboard
    )

    # Удаление клавиатуры
    await call.message.edit_reply_markup()

    # Выбор числа из диапазона и его сохранение
    my_num = randint(1, (await state.get_data())['num_range'] + 1)
    await state.update_data(my_num=int(my_num))

    # Перевод состояния на ввод первого числа
    await GuessingState.num_1.set()
