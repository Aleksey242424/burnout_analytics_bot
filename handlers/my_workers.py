from system_db import TableChief,TableWorkers,TableWorkerResponse,TableChiefResponse
from aiogram import types
class MyWorkers:
    def __init__(self,bot,call):
        self.bot = bot
        self.call = call
        self.table_chief = TableChief()
        self.table_workers = TableWorkers()
        self.table_worker_response = TableWorkerResponse()
        self.table_chief_response = TableChiefResponse()

    async def my_workers(self):
        workers = self.table_workers.select_workers(self.call.message.chat.id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        for worker in workers:
            username = worker[0]
            for _ in range(len(username)):
                if username[-1] != '_':
                    username = username[:-1]
                else:
                    username = username[:-1]
                    btn_worker = types.InlineKeyboardButton(text=f'{username}',callback_data=f'get_{worker[0]}')
                    markup.add(btn_worker)

        await self.bot.send_message(chat_id=self.call.message.chat.id,text='Ваши сотрудники',reply_markup=markup)