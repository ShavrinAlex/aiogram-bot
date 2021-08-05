from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import Message


def more_or_less_or_equal(message, my_num):
    '''
    Функция сравнивает загаданное ботом число с введенным пользователем и выводит значение сравнения.
    '''
    if message > my_num:
        return 'Загаданное число меньше'
    if message < my_num:
        return 'Загаданное число больше'
    if message == my_num:
        return 'Ура! Ты угадал моё число'

async def is_not_int(message: Message):
    """
    Функция проверяет: не является ли сообщения пользователя числом
    """
    if not (message.text.isdigit()):
        await message.reply(
            text='Это не число'
        )
        raise CancelHandler
