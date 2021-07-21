from math import log2
from random import randint
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loader import dp
from states.guessing import GuessingState


@dp.message_handler(state=GuessingState.num_range)
async def set_range(message: Message, state: FSMContext):

    # Проверка на число из предложенного списка
    if not (message.text in ['128', '256', '512', '1024']):
        await message.answer(
            text='Воспользуйтесь клавиатурой'
        )
        return False

    # Сохранение выбранного диапазона и кол-ва попыток
    await state.update_data(num_range=int(message.text))
    await state.update_data(attempt=int(log2((await state.get_data())['num_range'])))

    # Уведомление о кол-ве попыток
    await message.answer(
        text=f"У вас есть {int((await state.get_data())['attempt'])} попыток, чтобы отгадать загаданное мной число"
    )

    # Выбор числа из диапазона и его сохранение
    my_num = randint(1, (await state.get_data())['num_range'] + 1)
    await state.update_data(my_num=int(my_num))

    # Перевод состояния на ввод первого числа
    await GuessingState.num_1.set()
