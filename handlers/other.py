from aiogram import types, Dispatcher
import json, string
from create_bot import dp
import time

#@dp.message_handler()
async def rude(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply("``` Я ликидирую это СМС через 30 секунд, потому что здесь есть запретное слово.```", parse_mode='Markdown')
        time.sleep(5)
        await message.delete()
        await message.answer('``` Я удалил твоё грязное СМС! ```', parse_mode='Markdown')


#@dp.message_handler()
async def info_chat(message : types.Message):
    if message.text.lower() == 'инфа':

        #links = link('quinwize', 'https://t.me/lovesputin')
        await message.answer('*Бот был создан интеллегентом и гением - quinwize*,[quinwize](https://t.me/lovesputin) ', parse_mode="Markdown")



def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(rude)
    dp.register_message_handler(info_chat)

