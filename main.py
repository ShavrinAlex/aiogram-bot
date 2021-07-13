from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands='start')
async def eho(message: Message):
    await message.answer(
        text=f'Привет, {message.from_user.full_name}'
    )
    message_photo = await message.answer_photo(
        photo='https://c.wallhere.com/photos/8c/d7/cat_look_muzzle_lying_on_the_floor-629260.jpg!d'
    )
    await message.answer_photo(
        photo=message_photo.photo[0].file_id,
        caption=message_photo.photo[0].file_id
    )
    await message.answer_sticker(
        sticker='CAACAgIAAxkBAAECkTVg7DDRdxgSa1_s6M2fSVx0HLlYlwAC6QAD5bkIGk8D5NCmXq8dIAQ'
    )

def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()
