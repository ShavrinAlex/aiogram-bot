from aiogram.types import CallbackQuery
from keyboards.profile.inline.callback_datas import profile_callback
from loader import dp
from utils.db_api.tables.user import User


@dp.callback_query_handler(profile_callback.filter(operation_name='personal_area'))
async def personal_area(call: CallbackQuery):
    # Выводим информацию о пользователе
    await call.answer(cache_time=60)
    photos = (await call.from_user.get_profile_photos()).photos
    await call.message.answer_photo(
        photo=photos[0][-1].file_id,
        caption=f'{User.get_user(call.from_user.id)}'
    )

