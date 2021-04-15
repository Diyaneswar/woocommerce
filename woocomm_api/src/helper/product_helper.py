from woocomm_api.src.utilities.request_utility import Request_Utility

class Product_help(object):
    def __init__(self):
        self.req=Request_Utility()


    def get_product_by_id(self,product_id):

        return self.req.get(endpoint="products/{}".format(product_id))

