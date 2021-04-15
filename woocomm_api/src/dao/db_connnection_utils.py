import pymysql

class DB_connection():
    def __init__(self):
        pass

    def create_conn(self):
        db_conn=pymysql.connect(host='127.0.0.1',
                             user='root',password="mysql",port=3306)
        return db_conn

    def exec_conn(self,sql):
        conn=self.create_conn()
        try:
            cur=conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            re_db=cur.fetchall()
            cur.close()
        except Exception as E:
            raise Exception ("Failed to run sql query")
        finally:
            conn.close()

        return re_db


