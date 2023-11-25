from sqlite3 import connect,IntegrityError

class TableWorkers:
    def write(self,user_id,ref_id,username):
        with connect(r'burnout_analytics_bot/system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("BEGIN TRANSACTION;")
            username = f'''{username}#{TableWorkers().get_index_for_username(ref_id)}'''
            try:
                cursor.execute("""INSERT INTO workers(user_id,ref_id,username)
                           VALUES(?,?,?);""",(user_id,ref_id,username))
                cursor.execute("COMMIT;")
            except IntegrityError as ex:
                cursor.execute("ROLLBACK;")

    def get_index_for_username(self,ref_id):
        with connect(r'burnout_analytics_bot/system_db/db.db') as db:
            cursor = db.cursor()
            index = cursor.execute("""SELECT COUNT(worker_id) FROM workers
                           GROUP BY ref_id HAVING ref_id = ?""",(ref_id,)).fetchone()
            if index is not None:
                return index[0]
            return 0
        
    def select_workers(self,chief_id):
        with connect(r'burnout_analytics_bot/system_db/db.db') as db:
            cursor = db.cursor()
            workers = cursor.execute("""SELECT username FROM workers 
                           WHERE ref_id = ?""",(chief_id,)).fetchall()
            return workers
