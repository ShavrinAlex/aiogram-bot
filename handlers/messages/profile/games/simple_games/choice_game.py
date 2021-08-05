from aiogram.types import CallbackQuery
from keyboards.profile.games.inline.callback_datas import game_callback
from loader import dp
import keyboards


@dp.callback_query_handler(game_callback.filter(type_game='simple_games'))
async def games(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(
        text='Я могу бросить кубик или дротик',
        reply_markup=keyboards.profile.games.simple_games.keyboard
    )
