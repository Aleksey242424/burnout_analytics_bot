from sqlite3 import connect,IntegrityError


class TableTemp:
    def write(self,chief_id):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("""INSERT INTO temp(chief_id)
                           VALUES((SELECT chief_id FROM chief
                           WHERE user_id = ?))""",(chief_id,))
            
    def update_username_worker(self,chief_id,username):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("""UPDATE temp SET username_worker = ?
                           WHERE chief_id = (SELECT chief_id FROM chief
                           WHERE user_id = ?)""",
                           (username,chief_id))
            
    def update_date(self,chief,date):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("""UPDATE temp SET date""")

    def select_username_worker(self,chief_id):
        with connect(r'system_db\db.db') as db:
            cursor = db.cursor()
            username = cursor.execute("""SELECT username_worker FROM temp
                           WHERE chief_id = (SELECT chief_id FROM chief
                                      WHERE user_id = ?)""",(chief_id,)).fetchone()
            return username