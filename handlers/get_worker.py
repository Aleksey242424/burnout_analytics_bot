from system_db import TableWorkerResponse
from aiogram import types

class GetWorker:
    def __init__(self,bot,call):
        self.bot = bot
        self.call = call
        self.table_worker_response = TableWorkerResponse()

    async def get_worker(self):
        markup = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='Назад',callback_data='main_menu')
        username = self.call.data[4:]
        percent = self.table_worker_response.get_percent(username)
        markup.add(back)
        for _ in range(len(username)):
            if username[-1] != '_':
                username = username[:-1]
            else:
                username = username[:-1]
                break
        await self.bot.send_message(chat_id=self.call.message.chat.id,text=percent,reply_markup=markup)