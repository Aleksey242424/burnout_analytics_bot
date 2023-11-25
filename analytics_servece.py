from aiogram import types,executor
from create import Create
from handlers import Start
from handlers import QuestionForChief
from handlers import QuestionsForWorker
from handlers import MyWorkers
from handlers import GetWorker
from handlers import GetDateWorker
from handlers import MainMenu
from handlers import GetDataForWorker
from handlers import AddWorker
from handlers import Recomendations
from handlers import Right,Left

class AnalyticsServec(Create):
    def __init__(self):
        self.bot = super().bot
        self.dp = super().dp

    def process(self):
        @self.dp.message_handler(commands='start')
        async def start(message:types.Message):
            await Start(self.bot,message).start()

        @self.dp.callback_query_handler()
        async def callback(call:types.CallbackQuery):
            if call.data == 'questions_for_chief':
                await QuestionForChief(self.bot,self.dp,call).question_for_chief()

            if call.data == 'questions_for_worker':
                await QuestionsForWorker(self.bot,self.dp,call).questions_for_worker()

            if call.data == 'my_workers':
                await MyWorkers(self.bot,call).my_workers()

            if call.data[:4] == 'get_':
                await GetDateWorker(self.bot,call).get_date_worker()
                
            if call.data[:4] == 'get-':
                await GetWorker(self.bot,call).get_worker()

            if call.data[:4] == 'get:':
                await GetDataForWorker(self.bot,call).get_data_for_worker()

            if call.data == 'dates_worker':
                await GetDateWorker(self.bot,call).get_date_worker()

            if call.data == 'main_menu':
                await MainMenu(self.bot,call).main_menu()

            if call.data == 'add_worker':
                await AddWorker(self.bot,call).add_worker()

            if call.data == 'recommendation':
                await Recomendations(self.bot,call).recomendations()

            if call.data == 'right':
                await Right(self.bot,call).right()
            
            if call.data == 'left':
                await Left(self.bot,call).left()
                
        executor.start_polling(self.dp)
        