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
        for _ in range(len(username)):
            if username[-1] != '_':
                username = username[:-1]
            else:
                username = username[:-1]
                break
        if percent >= 50:
            recommendation = types.InlineKeyboardButton(text='Рекомендации',callback_data='recommendation')
            markup.add(recommendation)
            markup.add(back)
            await self.bot.send_message(chat_id=self.call.message.chat.id,text=f'<b>{percent}%</b>\nУ сотрудника замечены предпосылки к выгоранию. Вот наши советы к решению этой проблемы:',reply_markup = markup)
        else:
            markup.add(back)
            await self.bot.send_message(chat_id=self.call.message.chat.id,text=f'<b>{percent}%</b>',reply_markup = markup)