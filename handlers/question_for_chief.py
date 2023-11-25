from aiogram import types
from os import getenv
from dotenv import load_dotenv
from system_db import TableChiefResponse
from aiogram.dispatcher.storage import FSMContext
from fsm import StateForChief
from handlers import btn,markup_generate,btn_add_worker,btn_my_workers


class QuestionForChief:
    def __init__(self,bot,dp,call):
        self.bot = bot
        self.dp = dp
        self.call = call
        self.table_chief_response = TableChiefResponse()

    async def question_for_chief(self):
        await self.bot.send_message(chat_id=self.call.message.chat.id,text='Введите имя сотрудника')
        await StateForChief.username.set()
        @self.dp.message_handler(state=StateForChief.username)
        async def username_worker(message:types.Message,state=FSMContext):
            await state.update_data(username=message.text)
            btns = btn(1)
            markup = markup_generate(btns)
            await self.bot.send_message(chat_id=self.call.message.chat.id,text='Вопрос 1\nдля начальника',reply_markup=markup)
            await StateForChief.question_2.set()
        @self.dp.callback_query_handler(state=StateForChief.question_2)
        async def question_2_for_chief(call:types.CallbackQuery):
            if call.data[-1] == '1':
                if call.data == 'yes_1':
                    self.table_chief_response.write(chief_id=call.message.chat.id,question_num=1,response=1)
                else:
                    self.table_chief_response.write(chief_id=call.message.chat.id,question_num=1)
                btns = btn(2)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Вопрос 2\nдля начальника',reply_markup=markup)
                await StateForChief.question_3.set()
        @self.dp.callback_query_handler(state=StateForChief.question_3)
        async def question_3_for_chief(call:types.CallbackQuery):
            if call.data[-1] == '2':
                if call.data == 'yes_2':
                    self.table_chief_response.write(chief_id=call.message.chat.id,question_num=2,response=1)
                else:
                    self.table_chief_response.write(chief_id=call.message.chat.id,question_num=2)
                btns = btn(3)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Вопрос 3\nдля начальника',reply_markup=markup)
                await StateForChief.question_4.set()
        @self.dp.callback_query_handler(state=StateForChief.question_4)
        async def question_4_for_chief(call:types.CallbackQuery):
            if call.data[-1] == '3':
                if call.data == 'yes_3':
                    self.table_chief_response.write(chief_id=call.message.chat.id,question_num=3,response=1)
                else:
                    self.table_chief_response.write(chief_id=call.message.chat.id,question_num=3)
                btns = btn(4)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Вопрос 4\nдля начальника',reply_markup=markup)
                await StateForChief.question_5.set()
        @self.dp.callback_query_handler(state=StateForChief.question_5)
        async def question_5_for_chief(call:types.CallbackQuery,state=FSMContext):
            if call.data[-1] == '4':
                if call.data == 'yes_4':
                    self.table_chief_response.write(chief_id=call.message.chat.id,question_num=4,response=1)
                else:
                    self.table_chief_response.write(chief_id=call.message.chat.id,question_num=4)
                btns = btn(5)
                markup = markup_generate(btns)
                await self.bot.send_message(chat_id=call.message.chat.id,text='Вопрос 5\nдля начальника',reply_markup=markup)
                await StateForChief.result.set()
        @self.dp.callback_query_handler(state=StateForChief.result)
        async def result_for_chief(call:types.CallbackQuery,state=FSMContext):
            if call.data[-1] == '5':
                btns = [btn_my_workers,btn_add_worker]
                markup = markup_generate(btns)
                if call.data == 'yes_5':
                    self.table_chief_response.write(chief_id=call.message.chat.id,question_num=5,response=1)
                else:
                    self.table_chief_response.write(chief_id=call.message.chat.id,question_num=5)
                load_dotenv()
                data = await state.get_data()
                await self.bot.send_message(chat_id=call.message.chat.id,text='Вы завершили тест')
                await self.bot.send_message(chat_id=call.message.chat.id,text=f'Ваша реферальная ссылка\n<code>{getenv("LINK")}{call.message.chat.id}_{data["username"]}</code>',reply_markup=markup)
                await state.finish()