from woocomm_api.src.dao.db_connnection_utils import DB_connection
import random

class Get_customer_byemail():
    def __init__(self):
        self.db_con=DB_connection()

    def get_cust_by_email(self,email):
        sql="SELECT * FROM wp891.wpdi_users where user_email='{}'".format(email)
        db_resp=self.db_con.exec_conn(sql)
        return db_resp

    def get_cust_random_email(self):
        sql="SELECT * FROM wp891.wpdi_users order by id desc"
        user_list=self.db_con.exec_conn(sql)
        db_resp=random.sample(user_list,1)
        return db_resp

