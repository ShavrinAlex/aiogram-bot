from aiogram.types import Message, CallbackQuery
import keyboards.profile.games
from keyboards.profile.all_operation.callback_datas import profile_callback
from loader import dp


@dp.callback_query_handler(profile_callback.filter(operation_name='games'))
async def games(call: CallbackQuery):
    # Убираем часики
    await call.answer(cache_time=60)

    # Просим выбрать тип игры с выведеной клавиатуры
    await call.message.answer(
        text='Выберите тип игр:',
        reply_markup=keyboards.profile.games.inline.games.keyboard
    )
