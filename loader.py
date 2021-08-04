from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher(bot=bot, storage=MemoryStorage())
