from system_db import TableWorkerResponse,TableTemp
from aiogram import types

class GetDataForWorker:
    def __init__(self,bot,call):
        self.bot = bot
        self.call = call
        self.table_worker_response = TableWorkerResponse()

    async def get_data_for_worker(self):
        markup = types.InlineKeyboardMarkup(row_width=1)
        username = TableTemp().select_username_worker(self.call.message.chat.id)
        data = TableWorkerResponse().select_result_by_date(username,self.call.data[4:])
        back = types.InlineKeyboardButton(text='Назад',callback_data='main_menu')
        markup.add(back)
        await self.bot.send_message(chat_id=self.call.message.chat.id,text=f'{data[0]}',reply_markup = markup)