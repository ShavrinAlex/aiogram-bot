from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from handlers.messages.games.guessing.comparison import more_or_less_or_equal
from utils.db_api.tables.user import User


async def win(message: Message, state: FSMContext):
    """
    Функция выполняет действия при победе
    """
    # Присваиваем загаданное число и id пользователя переменным
    my_num = (await state.get_data())['my_num']
    user_id = message.from_user.id

    if User.is_user(user_id):
        await message.answer(
            text=f"{more_or_less_or_equal(int(message.text), my_num)}\n"
                 f"Вы выйграли 5 токенов"
        )
        User.cash_up(user_id, money=5)
    else:
        await message.answer(
            text=f"{more_or_less_or_equal(int(message.text), my_num)}\n"
                 f"Но вы не зарегестрированы, поэтому мы не можем начислить вам выйгрыш"
        )
    await state.finish()


async def not_win(message: Message, state: FSMContext):
    """
    Функция выполняет действия при не выйгрыше
    """
    # Присваиваем загаданное число переменной
    my_num = (await state.get_data())['my_num']
    await message.answer(
        text=f'{more_or_less_or_equal(int(message.text), my_num)}'
    )


async def losses(message: Message, state: FSMContext):
    """
    Функция выполняет действия при проигрыше
    """
    # Присваиваем id пользователя переменным
    user_id = message.from_user.id

    if User.is_user(user_id):
        await message.answer(
            text=f'Ничего страшного, тебе обязательно повезет в другой раз!\n'
                 f"A загаданное мной число было: {(await state.get_data())['my_num']}\n"
                 f"Вы проиграли 1 токен"
        )
        User.cash_down(user_id, money=1)
    else:
        await message.answer(
            text=f'Ничего страшного, тебе обязательно повезет в другой раз!\n'
                 f"A загаданное мной число было: {(await state.get_data())['my_num']}"
        )
    await state.finish()
