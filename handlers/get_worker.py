class GetWorker:
    def __init__(self,bot,call):
        self.bot = bot
        self.call = call

    async def get_worker(self):
        print(self.call.data[4:])