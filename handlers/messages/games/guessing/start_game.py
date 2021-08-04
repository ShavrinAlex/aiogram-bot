from aiogram.types import CallbackQuery
import keyboards
from keyboards.games.inline.callback_datas import game_callback
from loader import dp
from states.guessing import GuessingState
from utils.db_api.tables.user import User


@dp.callback_query_handler(game_callback.filter(type_game='guessing'))
async def start(call: CallbackQuery):
    # Предлагает выбрать диапазон чисел для загадывания из выведеной клавиатуры, если пользователь есть в базе данных
    if User.is_user(call.from_user.id):
        await call.message.edit_reply_markup()
        await call.message.answer(
            text='Выберите диапазон, в котором я загадаю число',
            reply_markup=keyboards.games.inline.guessing.keyboard
        )
        await GuessingState.num_range.set()
    else:
        await call.answer(
            text='Для участия в этой игре нужно быть зарегестрированным'
        )
