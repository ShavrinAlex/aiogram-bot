from aiogram import Dispatcher
from aiogram.types import BotCommand


commands = {
    'profile': 'Профиль',
    'registration': 'Регистрация'
}

async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            BotCommand(command=command, description=description) for command, description in commands.items()
        ]
    )
