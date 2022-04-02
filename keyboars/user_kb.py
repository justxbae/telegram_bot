from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
import emoji
b1 = KeyboardButton('Да!' + emoji.emojize(":beer_mug:"))
b2 = KeyboardButton('Информация о боте 🔒')
b3 = KeyboardButton('Причины выпить сегодня 🍷')
b4 = KeyboardButton('Вернуться назад ⚙')
b5 = KeyboardButton('Добавить бота в чат 🚬')
b6 = KeyboardButton('Личный кабинет 👤')
b7 = KeyboardButton('')
b8 = KeyboardButton('')
b9 = KeyboardButton('')
b10 = KeyboardButton('')



kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2)

kb_client_two = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_two.add(b3).add(b4)

kb_client_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_main.add(b3).insert(b5).add(b2).row(b6)