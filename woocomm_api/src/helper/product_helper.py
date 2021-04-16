from woocomm_api.src.utilities.request_utility import Request_Utility

class Product_help(object):
    def __init__(self):
        self.req=Request_Utility()


    def get_product_by_id(self,product_id):

        return self.req.get(endpoint=f"products/{product_id}",expected_status_code=201)

    def call_product_by_filter(self,payload):

        return self.req.get(endpoint=f"products",payload=payload)