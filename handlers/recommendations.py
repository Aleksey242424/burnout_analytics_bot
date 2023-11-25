from aiogram import types
from config import recommendtions_list
from system_db import TableTemp


class Recomendations:
    def __init__(self,bot,call):
        self.bot = bot
        self.call = call
        self.table_temp = TableTemp()

    async def recomendations(self):
        recom = recommendtions_list[0]
        self.table_temp.update_page(self.call.message.chat.id,0)
        markup = types.InlineKeyboardMarkup(row_width=1)
        right = types.InlineKeyboardButton(text='>>',callback_data='right')
        back = types.InlineKeyboardButton(text='Назад',callback_data='main_menu')
        markup.add(right)
        markup.add(back)
        await self.bot.send_message(chat_id=self.call.message.chat.id,text=f'{recom}',reply_markup = markup)