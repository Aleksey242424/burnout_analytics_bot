from sqlite3 import connect,IntegrityError

class TableChiefResponse:
    def write(self,chief_id,question_num,response=0):
        with connect(r'burnout_analytics_bot/system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("BEGIN TRANSACTION;")
            try:
                cursor.execute("""INSERT INTO chief_respons(chief_id,response,question_num)
                           VALUES((SELECT chief_id FROM chief WHERE user_id = ?),?,?)""",
                           (chief_id,response,question_num))
                cursor.execute("COMMIT;")
            except IntegrityError as ex:
                cursor.execute("ROLLBACK;")


    def delete(self,user_id):
        with connect(r'burnout_analytics_bot/system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("""DELETE FROM chief_respons WHERE chief_id = (SELECT chief_id FROM chief WHERE user_id = ?)""",(user_id,))
    