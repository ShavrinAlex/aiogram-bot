from aiogram.types import Message
from loader import dp
from utils.db_api.tables.user import User


@dp.message_handler(commands='registration')
async def start(message: Message):
    # В случае отсутствия пользователя в базе данных регестрируем его
    if User.is_user(message.from_user.id):
        await message.answer(text='Вы уже зарегестрированны')
    else:
        user = User(
            id=message.from_user.id,
            username=message.from_user.username,
            fullname=message.from_user.full_name
        )
        await message.answer(text='Регистрация прошла успешно!')
