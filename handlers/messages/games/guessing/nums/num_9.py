from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from handlers.messages.games.guessing.actions import losses, win, not_win
from loader import dp
from states.guessing import GuessingState
from handlers.messages.games.guessing.comparison import more_or_less_or_equal, is_not_int


@dp.message_handler(state=GuessingState.num_9)
async def num_9(message: Message, state: FSMContext):
    # Присваиваем загаданное число переменной
    my_num = (await state.get_data())['my_num']

    # Присваиваем кол-во попыток переменной
    attempt = (await state.get_data())['attempt']

    # Проверяем: не является ли сообщение числом
    await is_not_int(message)

    # Проверяем: является ли эта попытка последней
    if attempt == 9:
        # Проверяем: не угадал ли пользователь число
        if more_or_less_or_equal(int(message.text), my_num) != 'Ура! Ты угадал моё число':
            await losses(message, state)
            return False
        else:
            await win(message, state)
            return False
    else:
        # Проверяем: угадал ли пользователь число
        if more_or_less_or_equal(int(message.text), my_num) == 'Ура! Ты угадал моё число':
            await win(message, state)
        else:
            await not_win(message, state)
            await GuessingState.num_10.set()
