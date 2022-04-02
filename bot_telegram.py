from aiogram.utils import executor
from create_bot import dp

async def on_startup(_):
   print('Бот работает.')

from handlers import other, user_part

user_part.register_handlers_user(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
