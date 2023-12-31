from sqlite3 import connect,IntegrityError

class TableChiefResponse:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def write(self,chief_id,question_num,response=0):
        with connect(r'system_db/db.db') as db:
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
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("""DELETE FROM chief_respons WHERE chief_id = (SELECT chief_id FROM chief WHERE user_id = ?)""",(user_id,))
    
    def select_count_response(self,user_id):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            count_response = cursor.execute("""SELECT COUNT(response) FROM chief_respons
                           WHERE chief_id = (SELECT chief_id FROM chief WHERE user_id = ?)
                           AND response = 1""",(user_id,)).fetchone()
            return count_response[0]