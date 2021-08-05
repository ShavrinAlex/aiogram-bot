from aiogram.types import CallbackQuery
import keyboards
from keyboards.profile.games.inline.callback_datas import game_callback
from loader import dp
from states.guessing import GuessingState


@dp.callback_query_handler(game_callback.filter(type_game='guessing'))
async def start(call: CallbackQuery):
    # Предлагает выбрать диапазон чисел для загадывания из выведеной клавиатуры
    await call.message.edit_reply_markup()
    await call.message.answer(
        text='Выберите диапазон, в котором я загадаю число',
        reply_markup=keyboards.profile.games.inline.guessing.keyboard
    )
    await GuessingState.num_range.set()
