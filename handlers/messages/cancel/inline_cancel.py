from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.cancel.callback_datas import cancel_callback
from loader import dp


@dp.callback_query_handler(cancel_callback.filter(operation_name='cancel'), state='*')
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.answer(
        text='Вы перемещены в главное меню',
        show_alert=True
    )
    await call.message.edit_reply_markup()
    await state.finish()
