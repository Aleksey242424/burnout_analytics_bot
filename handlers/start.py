from aiogram import types
from system_db import TableChief,TableWorkers,TableChiefResponse,TableWorkerResponse
from handlers import btn_start_for_worker,btn_start_for_chief
from handlers.check_referrals import check_referrals


class Start:
    def __init__(self,bot,message):
        self.bot = bot
        self.message = message
        self.table_chief = TableChief()
        self.table_worker = TableWorkers()
        self.table_chief_response = TableChiefResponse()
        self.table_worker_response = TableWorkerResponse()

    async def start(self):
        markup = types.InlineKeyboardMarkup(row_width=1)
        data = self.message.text[7:]
        if data:
            data = data.split('_')
            print(data)
            ref_id = data[0]
            print(ref_id)
            username = data[1]
            if check_referrals(ref_id,str(self.message.chat.id)):

                self.table_worker.update_user_id(self.message.chat.id,f'{username}_{data[2]}')
                print(f'{username}_{data[2]}')
                markup.add(btn_start_for_worker)
                self.table_worker_response.delete(self.message.chat.id)
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