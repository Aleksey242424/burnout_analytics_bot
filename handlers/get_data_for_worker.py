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
        if data[0] >= 50:
            recommendation = types.InlineKeyboardButton(text='Рекомендации',callback_data='recommendation')
            markup.add(recommendation)
            markup.add(back)
            await self.bot.send_message(chat_id=self.call.message.chat.id,text=f'<b>{data[0]}%</b>\nУ сотрудника замечены предпосылки к выгоранию. Вот наши советы к решению этой проблемы:',reply_markup = markup)
        else:
            markup.add(back)
            await self.bot.send_message(chat_id=self.call.message.chat.id,text=f'<b>{data[0]}%</b>',reply_markup = markup)