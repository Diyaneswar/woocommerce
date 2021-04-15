from woocomm_api.src.utilities.request_utility import Request_Utility

class Customer_help(object):
    def __init__(self):
        self.req=Request_Utility()

    def create_customer(self,email,password,**kwargs):
        #creating payload
        payload={}
        payload["email"]=email
        payload["password"]=password
        payload.update(**kwargs)

        headers = {"Content-Type": "application/json"}

        resp=self.req.post("customers",payload,headers,expected_statuscode=201)

        return resp.json()






