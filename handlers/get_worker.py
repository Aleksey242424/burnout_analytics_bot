from system_db import TableWorkerResponse


class GetWorker:
    def __init__(self,bot,call):
        self.bot = bot
        self.call = call
        self.table_worker_response = TableWorkerResponse()

    async def get_worker(self):
        username = self.call.data[4:]
        percent = self.table_worker_response.get_percent(username)
        for _ in range(len(username)):
            if username[-1] != '_':
                username = username[:-1]
            else:
                username = username[:-1]
                break
        await self.bot.send_message(chat_id=self.call.message.chat.id,text=percent)