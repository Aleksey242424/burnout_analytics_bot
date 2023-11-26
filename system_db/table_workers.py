from sqlite3 import connect,IntegrityError

class TableWorkers:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def write(self,ref_id,username):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("BEGIN TRANSACTION;")
            try:
                cursor.execute("""INSERT INTO workers(ref_id,username)
                           VALUES((SELECT chief_id FROM chief WHERE user_id = ?),?);""",(ref_id,username))
                cursor.execute("COMMIT;")
            except IntegrityError as ex:
                print(ex)
                cursor.execute("ROLLBACK;")

    def update_user_id(self,user_id,username):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("""UPDATE workers SET user_id=? WHERE username = ?""",(user_id,username))

    def get_index_for_username(self,ref_id):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            index = cursor.execute("""SELECT COUNT(worker_id) FROM workers
                           GROUP BY ref_id HAVING ref_id = (SELECT chief_id FROM chief
                                   WHERE user_id = ?)""",(ref_id,)).fetchone()
            if index is not None:
                return index[0]
            return 0
        
    def select_workers(self,chief_id):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            workers = cursor.execute("""SELECT username FROM workers 
                           WHERE ref_id = (SELECT chief_id FROM chief WHERE user_id = ?)""",(chief_id,)).fetchall()
            return workers
        
    def select_chief_id(self,user_id):
        with connect(r"system_db/db.db") as db:
            cursor = db.cursor()
            ref_id = cursor.execute("""SELECT ref_id FROM workers WHERE user_id = ?""",(user_id,)
                                    ).fetchone()
            return ref_id[0]
    def select_username(self,user_id):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            username = cursor.execute("""SELECt username FROM workers
                           WHERE user_id = ?""",
                           (user_id,)).fetchone()
            return username[0]
        
