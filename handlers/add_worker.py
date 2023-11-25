from aiogram import types
from aiogram import types
from system_db import TableChief,TableWorkers,TableChiefResponse,TableWorkerResponse,TableTemp
from handlers import btn_start_for_chief

class AddWorker:
    def __init__(self,bot,call):
        self.bot = bot
        self.call = call
        self.table_chief_response = TableChiefResponse()

    async def add_worker(self):
        markup = types.InlineKeyboardMarkup(row_width=1)
        self.table_chief_response.delete(self.call.message.chat.id)
        markup.add(btn_start_for_chief)
        await self.bot.send_message(chat_id=self.call.message.chat.id,text='Тест для аналитике выгораемости сотрудника',reply_markup=markup)