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

