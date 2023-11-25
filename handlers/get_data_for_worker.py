from system_db import TableWorkerResponse,TableTemp


class GetDataForWorker:
    def __init__(self,bot,call):
        self.bot = bot
        self.call = call
        self.table_worker_response = TableWorkerResponse()

    async def get_data_for_worker(self):
        username = TableTemp().select_username_worker(self.call.message.chat.id)
        data = TableWorkerResponse().select_result_by_date(username,self.call.data[4:])

        await self.bot.send_message(chat_id=self.call.message.chat.id,text=f'{data[1]}\n\n{data[0]}')