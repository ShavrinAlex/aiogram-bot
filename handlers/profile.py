from aiogram.types import Message
from loader import dp

@dp.message_handler(text='Личный кабинет')
async def menu_profile(message: Message):
    photos = (await message.from_user.get_profile_photos()).photos
    await message.answer_photo(
        photo=photos[0][-1].file_id,
        caption=f'Имя: {message.from_user.first_name}\n'
                f'ID: {message.from_user.id}\n'
                f'Username: @{message.from_user.username}'
        )
