from sqlite3 import connect,IntegrityError


class TableWorkerResponse:
    def write(self,worker_id,question_num,response=0):
        with connect(r'burnout_analytics_bot/system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("BEGIN TRANSACTION;")
            try:
                cursor.execute("""INSERT INTO worker_response(worker_id,response,question_num)
                           VALUES((SELECT worker_id FROM workers WHERE user_id = ?),?,?)""",(worker_id,response,question_num))
                cursor.execute("COMMIT;")
            except IntegrityError as ex:
                cursor.execute("ROLLBACK;")

    def select_result(self,username):
        with connect(r'burnout_analytics_bot/system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("""SELECT """)