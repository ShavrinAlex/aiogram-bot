from aiogram.types import Message
from loader import dp
import keyboards
from utils.db_api.tables.user import User


@dp.message_handler(commands='profile')
async def start(message: Message):
    # Приветствуем и выводим кнопки профиля если пользователь зарегестрирован
    if User.is_user(message.from_user.id):
        await message.answer(
            text=f'Привет, {message.from_user.full_name}',
            reply_markup=keyboards.profile.all_operation.profile_operation.keyboard
        )
    else:
        await message.answer(
            text='Зарегестрируйтесь, чтобы получить доступ к профилю'
        )
