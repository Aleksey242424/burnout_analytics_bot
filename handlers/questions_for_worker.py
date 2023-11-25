from aiogram import types
from system_db import TableWorkerResponse,TableWorkers,TableChief
from aiogram.dispatcher.storage import FSMContext
from fsm import StateForWorker
from handlers import btn,markup_generate


class QuestionsForWorker:
    def __init__(self,bot,dp,call):
        self.bot = bot
        self.dp = dp
        self.call = call
        self.table_worker_response = TableWorkerResponse()
        self.table_workers = TableWorkers()
        self.table_chief = TableChief()
    
    async def questions_for_worker(self):
        btns = btn(1)
        markup = markup_generate(btns)
        await self.bot.send_message(chat_id=self.call.message.chat.id,text='Чувствуете ли вы себя измотанным и истощенным, как физически, так и психически, большую часть времени?',reply_markup=markup)
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
                await self.bot.send_message(chat_id=call.message.chat.id,text='Становитесь ли вы все более циничным и отстраненным от своей работы?',reply_markup=markup)
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
                await self.bot.send_message(chat_id=call.message.chat.id,text='Чувствуете ли Вы недостаток достижений и продуктивности, несмотря на долгие часы работы?',reply_markup=markup)
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
                await self.bot.send_message(chat_id=call.message.chat.id,text='Чувствуете ли Вы, что Вам постоянно приходится справляться с нагрузкой?',reply_markup=markup)
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
                await self.bot.send_message(chat_id=call.message.chat.id,text='Чувствуете ли Вы, что больше не в состоянии соответствовать ожиданиям от своей работы?',reply_markup=markup)
                await StateForWorker.question_6.set()
        @self.dp.callback_query_handler(state=StateForWorker.question_6)
        async def question_6_for_worker(call:types.CallbackQuery):
            if call.data[-1] == '5':
                if call.data == 'yes_5':
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=5,response=1)
                else:
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=5)
                btns = btn(6)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Чувствуете ли Вы, что постоянно находитесь под давлением и испытываете стресс?',reply_markup=markup)
                await StateForWorker.question_7.set()
        @self.dp.callback_query_handler(state=StateForWorker.question_7)
        async def question_5_for_worker(call:types.CallbackQuery):
            if call.data[-1] == '6':
                if call.data == 'yes_6':
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=6,response=1)
                else:
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=6)
                btns = btn(7)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Чувствуете ли Вы, что не можете делать перерывы и отвлекаться от работы, когда это необходимо?',reply_markup=markup)
                await StateForWorker.question_8.set()
        @self.dp.callback_query_handler(state=StateForWorker.question_8)
        async def question_5_for_worker(call:types.CallbackQuery):
            if call.data[-1] == '7':
                if call.data == 'yes_7':
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=7,response=1)
                else:
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=7)
                btns = btn(8)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Чувствуете ли Вы, что не можете эффективно совмещать работу и личную жизнь?',reply_markup=markup)
                await StateForWorker.question_9.set()
        @self.dp.callback_query_handler(state=StateForWorker.question_9)
        async def question_5_for_worker(call:types.CallbackQuery):
            if call.data[-1] == '8':
                if call.data == 'yes_8':
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=8,response=1)
                else:
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=8)
                btns = btn(9)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Считаете ли Вы, что не можете донести свои проблемы и потребности до руководителя или коллег?',reply_markup=markup)
                await StateForWorker.question_10.set()
        @self.dp.callback_query_handler(state=StateForWorker.question_10)
        async def question_5_for_worker(call:types.CallbackQuery):
            if call.data[-1] == '9':
                if call.data == 'yes_9':
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=9,response=1)
                else:
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=9)
                btns = btn(10)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Считаете ли Вы, что Вас не ценят и не признают Ваш вклад в работу?',reply_markup=markup)
                await StateForWorker.result.set()
        @self.dp.callback_query_handler(state=StateForWorker.result)
        async def result_for_worker(call:types.CallbackQuery,state=FSMContext):
            if call.data[-1] == '0':
                if call.data == 'yes_10':
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=10,response=1)
                else:
                    self.table_worker_response.write(worker_id=call.message.chat.id,question_num=10)
                if self.table_worker_response.select_result(call.message.chat.id) >= 5:
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    username = self.table_workers.select_username(call.message.chat.id)
                    result = types.InlineKeyboardButton(text='Посмотреть результаты',callback_data=f'get-{username}')
                    markup.add(result)
                    for _ in range(len(username)):
                        if username[-1] != '_':
                            username = username[:-1]
                        else:
                            username = username[:-1]
                            break
                    chief_id = self.table_chief.select_id(call.message.chat.id)
                    await self.bot.send_message(chat_id=int(chief_id),text=f'Ваш сотрудник {username} окончил тест',reply_markup=markup)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Вы закончили тест.\nПерспектива для выгориния "Какой-то процент%"\nВашему начальнику придут результаты')
                await state.finish()