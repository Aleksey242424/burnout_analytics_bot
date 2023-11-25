from aiogram import types
from system_db import TableChief,TableWorkers,TableChiefResponse
from handlers import btn_start_for_worker,btn_start_for_chief
from handlers.check_referrals import check_referrals


class Start:
    def __init__(self,bot,message):
        self.bot = bot
        self.message = message
        self.table_chief = TableChief()
        self.table_worker = TableWorkers()
        self.table_chief_response = TableChiefResponse()

    async def start(self):
        markup = types.InlineKeyboardMarkup(row_width=1)
        data = self.message.text[7:]
        if data:
            username = ''
            ref_id = ''
            for _ in data:
                if data[0] != '_':
                    ref_id = f'{ref_id}{data[0]}'
                    data = data[1:]
                else:
                    data = data[1:]
                    username = data
                    break
            if check_referrals(ref_id,str(self.message.chat.id)):
                self.table_worker.write(self.message.chat.id,ref_id,username)
                markup.add(btn_start_for_worker)
                await self.bot.send_message(chat_id=self.message.chat.id,text='Ваш начальник выслал вам тест',reply_markup=markup)
            else:
                self.table_chief.write(self.message.chat.id)
                self.table_chief_response.delete(self.message.chat.id)
                markup.add(btn_start_for_chief)
                await self.bot.send_message(chat_id=self.message.chat.id,text='Здравствуйте, я бот для определения рисков выгорания у сотрудника',reply_markup=markup)
        else:
            self.table_chief.write(self.message.chat.id)
            self.table_chief_response.delete(self.message.chat.id)
            markup.add(btn_start_for_chief)
            await self.bot.send_message(chat_id=self.message.chat.id,text='Тест для аналитике выгораемости сотрудника',reply_markup=markup)