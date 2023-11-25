from aiogram import Bot,Dispatcher
from os import getenv
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

class Create:
    load_dotenv()
    bot = Bot(token = getenv('API_TOKEN'),parse_mode='HTML')
    dp = Dispatcher(bot = bot,storage=MemoryStorage())
