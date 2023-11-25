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
    