
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboars import kb_client, kb_client_two, kb_client_main
from aiogram.utils.markdown import link





@dp.message_handler(commands=["start"])
async def commands_start(message : types.Message):
   try:
      await bot.send_message(message.from_user.id, '➖➖➖➖➖➖➖➖➖➖\nСветлана,добрый день. А вы уже готовы пойти напер?\n \
     Если да, то нажимай скорее "Да". Если нет, то пожалуйста покиньте этого бота. Мы против трезвенников...\n➖➖➖➖➖➖➖➖➖➖', reply_markup=kb_client)
   except:
    await message.reply('Чтобы я мог написать тебе ответить, сперва напиши мне:\n@buhhoy_bot')




@dp.message_handler(lambda message: message.text == "Да!🍺")
async def agreement(message: types.Message):
   await message.reply("🇷🇺Не можешь найти повода выпить?🍺\nНе проблема. \n💥Жми на кнопку, и бухай сколько угодно!💥", reply_markup=kb_client_two)



@dp.message_handler(lambda message: message.text == 'Вернуться назад ⚙')
async def back(msg: types.Message):
    reply_text = "Главное меню"
    await msg.answer(reply_text, reply_markup=kb_client_main)


@dp.message_handler(lambda message: message.text == 'В меню')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Вернуться')
    await message.answer("Вот меню", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'Информация о боте 🔒')
async def info(message: types.Message):
    text = link('quinwize', 'https://t.me/lovesputin')
    await message.reply('*Бот был создан интеллегентом и гением - *' + text, parse_mode="Markdown")


@dp.message_handler(lambda message: message.text == 'инфа')
async def info_chat(message : types.Message):
    if message.text.lower() == 'инфа':

        #links = link('quinwize', 'https://t.me/lovesputin')
        await message.answer('*Бот был создан интеллегентом и гением - *[quinwize](https://t.me/lovesputin) ', parse_mode="Markdown")
























def register_handlers_user(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])








'''
@dp.message_handler()
async def echo_send(message : types.Message):
    await message.reply(message.text)
    '''


