from sqlite3 import connect,IntegrityError

class TableChief:
    def write(self,user_id):
        with connect(r'burnout_analytics_bot/system_db/db.db') as db:
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
        with connect(r'burnout_analytics_bot/system_db/db.db') as db:
            cursor = db.cursor()
            user_id = cursor.execute("""SELECT user_id FROM chief WHERE chief_id = (SELECT chief_id FROM workers
                           WHERE user_id = ?)""",(worker_id,)).fetchone()
            return user_id[0]