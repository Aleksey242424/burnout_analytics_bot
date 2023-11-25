from aiogram import types
from system_db import TableWorkerResponse
from aiogram.dispatcher.storage import FSMContext
from fsm import StateForWorker
from handlers import btn,markup_generate


class QuestionsForWorker:
    def __init__(self,bot,dp,call):
        self.bot = bot
        self.dp = dp
        self.call = call
        self.table_worker_response = TableWorkerResponse()
    
    async def questions_for_worker(self):
        btns = btn(1)
        markup = markup_generate(btns)
        await self.bot.send_message(chat_id=self.call.message.chat.id,text='Вопрос 1\nдля работника',reply_markup=markup)
        await StateForWorker.question_2.set()
        @self.dp.callback_query_handler(state=StateForWorker.question_2)
        async def question_2_for_worker(call:types.CallbackQuery):
            if call.data[-1] == '1':
                if call.data == 'yes_1':
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=1,response=1)
                else:
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=1)
                btns = btn(2)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Вопрос 2\nдля работника',reply_markup=markup)
                await StateForWorker.question_3.set()
        @self.dp.callback_query_handler(state=StateForWorker.question_3)
        async def question_3_for_worker(call:types.CallbackQuery):
            if call.data[-1] == '2':
                if call.data == 'yes_2':
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=2,response=1)
                else:
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=2)
                btns = btn(3)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Вопрос 3\nдля работника',reply_markup=markup)
                await StateForWorker.question_4.set()
        @self.dp.callback_query_handler(state=StateForWorker.question_4)
        async def question_4_for_worker(call:types.CallbackQuery):
            if call.data[-1] == '3':
                if call.data == 'yes_3':
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=3,response=1)
                else:
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=3)
                btns = btn(4)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Вопрос 4\nдля работника',reply_markup=markup)
                await StateForWorker.question_5.set()
        @self.dp.callback_query_handler(state=StateForWorker.question_5)
        async def question_5_for_worker(call:types.CallbackQuery):
            if call.data[-1] == '4':
                if call.data == 'yes_4':
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=4,response=1)
                else:
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=4)
                btns = btn(5)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Вопрос 5\nдля работника',reply_markup=markup)
                await StateForWorker.result.set()
        @self.dp.callback_query_handler(state=StateForWorker.result)
        async def result_for_worker(call:types.CallbackQuery,state=FSMContext):
            if call.data[-1] == '5':
                if call.data == 'yes_5':
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=5,response=1)
                else:
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=5)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Вы закончили тест.\nПерспектива для выгориния "Какой-то процент%"\nВашему начальнику придут результаты')
                await state.finish()