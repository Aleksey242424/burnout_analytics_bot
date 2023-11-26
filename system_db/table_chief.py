from sqlite3 import connect,IntegrityError


class TableChief:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def write(self,user_id):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("BEGIN TRANSACTION;")
            try:
                cursor.execute('''INSERT INTO chief(user_id)
                           VALUES(?);''',
                           (user_id,))
                cursor.execute("COMMIT;")
            except IntegrityError as ex:
                cursor.execute("ROLLBACK;")


    def select_id(self,worker_id):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            user_id = cursor.execute("""SELECT user_id FROM chief WHERE chief_id = (SELECT ref_id FROM workers
                           WHERE user_id = ?)""",(worker_id,)).fetchone()
            return user_id[0]