from aiogram import types
from config import recommendtions_list
from system_db import TableTemp

class Left:
    def __init__(self,bot,call):
        self.bot = bot
        self.call = call
        self.table_temp = TableTemp()

    async def left(self):
        page = self.table_temp.select_page(self.call.message.chat.id) - 1
        self.table_temp.update_page(self.call.message.chat.id,page)
        recom = recommendtions_list[page]
        markup = types.InlineKeyboardMarkup(row_width=2)
        right = types.InlineKeyboardButton(text='>>',callback_data='right')
        if page>0:
            left = types.InlineKeyboardButton(text='<<',callback_data='left')
            markup.add(left,right)
        else:
            markup.add(right)
        back = types.InlineKeyboardButton(text='Назад',callback_data='main_menu')
        markup.add(back)
        await self.bot.send_message(chat_id=self.call.message.chat.id,text=recom,reply_markup=markup)