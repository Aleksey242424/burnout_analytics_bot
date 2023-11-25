from system_db import TableWorkerResponse
from aiogram import types

class GetDateWorker:
    def __init__(self,bot,call):
        self.bot = bot
        self.call = call
        self.table_worker_response = TableWorkerResponse()

    async def get_date_worker(self):
        markup = types.InlineKeyboardMarkup(row_width=1)
        username = self.call.data[4:]
        dates = self.table_worker_response.select_date(username)
        for date in dates:
            btn_date = types.InlineKeyboardButton(text=f'{date[0]}',callback_data=f'{date[0]}')
            markup.add(btn_date)
        await self.bot.send_message(chat_id=self.call.message.chat.id,text='Даты провождения теста',reply_markup = markup)