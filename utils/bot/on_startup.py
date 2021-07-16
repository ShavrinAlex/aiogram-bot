from aiogram import Dispatcher
from .set_bot_command import set_commands


async def on_startup(dp: Dispatcher):
    await dp.bot.send_message(
        chat_id=1369534986,
        text='Бот активирован'
    )
    await set_commands(dp)