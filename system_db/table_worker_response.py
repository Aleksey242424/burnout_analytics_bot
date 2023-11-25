from sqlite3 import connect,IntegrityError
from DateTime import DateTime


class TableWorkerResponse:
    def write(self,worker_id,question_num,response=0):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            cursor.execute("BEGIN TRANSACTION;")
            date = DateTime().Date()
            try:
                cursor.execute("""INSERT INTO worker_response(worker_id,response,question_num,date_response)
                           VALUES((SELECT worker_id FROM workers WHERE user_id = ?),?,?,?)""",(worker_id,response,question_num,date))
                cursor.execute("COMMIT;")
            except IntegrityError as ex:
                cursor.execute("ROLLBACK;")

    def select_result(self,user_id):
        with connect(r'system_db/db.db') as db:
            cursor = db.cursor()
            count_response = cursor.execute("""SELECT COUNT(response) FROM worker_response
                           WHERE worker_id = (SELECT worker_id FROM workers
                           WHERE user_id = ?) AND response = 1""",(user_id,)
                           ).fetchone()
            return count_response[0]
        
    def get_percent(self,username):
        with connect(r'system_db\db.db') as db:
            cursor = db.cursor()
            count_response = cursor.execute("""SELECT COUNT(response),date_response FROM worker_response WHERE response = 1 AND
                           worker_id = (SELECT worker_id FROM workers WHERE 
                           username = ?) GROUP BY date_response""",(username,)).fetchone()
            print(count_response,type(count_response))
            print(username)
            percent = count_response[0]*10
            return f'{percent}%'
        
    def select_date(self,username):
        with connect(r'system_db\db.db') as db:
            cursor = db.cursor()
            dates = cursor.execute("""SELECT date_response FROM worker_response
                                   WHERE worker_id = (
                           SELECT worker_id FROM workers WHERE username = ?
                           )
                           GROUP BY date_response""",(username,)).fetchall()
            print(username)
            return dates
        
    def delete(self,user_id):
        with connect(r'system_db\db.db') as db:
            date = DateTime().Date()
            cursor = db.cursor()
            cursor.execute("""DELETE FROM worker_response WHERE worker_id = 
                           (SELECT worker_id FROM workers WHERE user_id = ?) AND date_response = ?""",
                           (user_id,date))


    def select_result_by_date(self,username,date):
        with connect(r"system_db\db.db") as db:
            cursor = db.cursor()
            print(username)
            result = cursor.execute("""SELECT COUNT(date_response),date_response FROM worker_response
                           WHERE worker_id = (
                           SELECT worker_id FROM workers WHERE username = ?
                           )
                           AND date_response = ?""",
                           (username[0],date)
                           ).fetchone()
            percent = f"{result[0]*10}%"
            return percent,result[1]
            
        