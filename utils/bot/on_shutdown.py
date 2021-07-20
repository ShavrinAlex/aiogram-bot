from aiogram import Dispatcher


async def on_shutdown(dp: Dispatcher):
    await dp.bot.send_message(
        chat_id=1369534986,
        text='Бот выключен'
    )
