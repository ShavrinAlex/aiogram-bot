from aiogram.types import Message
from loader import dp


@dp.message_handler(text='Личный кабинет')
async def personal_area(message: Message):
    photos = (await message.from_user.get_profile_photos()).photos
    await message.answer_photo(
        photo=photos[0][-1].file_id,
        caption=f'Имя пользователя: {message.from_user.full_name}\n'
                f'ID: {message.from_user.id}\n'
                f'Username: @{message.from_user.username}'
    )
