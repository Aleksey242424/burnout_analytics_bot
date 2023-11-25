from system_db import TableChief,TableWorkers,TableWorkerResponse,TableChiefResponse

class DBInit:
    def __init__(self):
        self.table_chief = TableChief()
        self.table_workers = TableWorkers()
        self.table_worker_response = TableWorkerResponse()
        self.table_chief_response = TableChiefResponse()