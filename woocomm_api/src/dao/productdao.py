import random
from woocomm_api.src.dao.db_connnection_utils import DB_connection

class Productdao():
    def __init__(self):
        self.db_con=DB_connection()

    def get_random_prd(self):
        sql='select * FROM wp891.wpdi_posts where post_type="product";'
        db_out=self.db_con.exec_conn(sql)
        rand_product=random.sample(db_out,1)
        return rand_product

    def create_product_call(self,product_id):
        sql=f'select * FROM wp891.wpdi_posts where ID="{product_id}";'
        return self.db_con.exec_conn(sql)


    def get_product_using_filter(self,_date):
        sql= f"select * From wp891.wpdi_posts where post_type='products' AND post_date > '{_date}';"
        return self.db_con.exec_conn(sql)
