from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from handlers.messages.profile.games.guessing.actions import win, not_win
from loader import dp
from states.guessing import GuessingState
from handlers.messages.profile.games.guessing.comparison import more_or_less_or_equal, is_not_int


@dp.message_handler(state=GuessingState.num_3)
async def num_3(message: Message, state: FSMContext):
    # Присваиваем загаданное число переменной
    my_num = (await state.get_data())['my_num']

    # Проверяем: не является ли сообщение числом
    await is_not_int(message)

    # Проверяем: угадал ли пользователь число
    if more_or_less_or_equal(int(message.text), my_num) == 'Ура! Ты угадал моё число':
       await win(message, state)
    else:
        await not_win(message, state)
        await GuessingState.num_4.set()
