from aiogram.types import Message
from loader import dp
from utils.db_api.tables.user import User


@dp.message_handler(text='Личный кабинет')
async def personal_area(message: Message):
    # При наличии пользователя в базе данных выводим информацию о нем
    if User.is_user(message.from_user.id):
        photos = (await message.from_user.get_profile_photos()).photos
        await message.answer_photo(
            photo=photos[0][-1].file_id,
            caption=f'{User.get_user(message.from_user.id)}'
        )
    else:
        await message.answer(
            text='Зарегестрируйтесь, чтобы получить данные'
        )

