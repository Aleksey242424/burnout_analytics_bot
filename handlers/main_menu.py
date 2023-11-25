from aiogram import types


class MainMenu:
    def __init__(self,bot,call):
        self.bot = bot
        self.call = call

    async def main_menu(self):
        markup = types.InlineKeyboardMarkup(row_width=1)
        my_worker = types.InlineKeyboardButton(text='Мои сотрудники',callback_data='my_workers')
        add_worker = types.InlineKeyboardButton(text='Добавить',callback_data='add_worker')
        markup.add(my_worker,add_worker)
        await self.bot.send_message(chat_id=self.call.message.chat.id,text='Главное меню',reply_markup=markup)