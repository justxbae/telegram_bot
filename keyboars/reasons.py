            #   Причины выпить сегодня 🍷

from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboars import kb_client, kb_client_two, kb_client_main
from aiogram.utils.markdown import link



@dp.message_handler(lambda message: message.text == 'Вернуться назад ⚙')
async def reason_button(msg: types.Message):
    reply_text = "Главное меню"
    await msg.answer(reply_text, reply_markup=kb_client_main)








def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(reason_button)