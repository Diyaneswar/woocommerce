import requests
import json
import logging as logger
from requests_oauthlib import OAuth1
from woocomm_api.src.utilities.credential_utility import Credential

class Request_Utility(object):
    def __init__(self):
        cred=Credential.generate_cred()
        self.baseurl="http://127.0.0.1/wp/wp-json/wc/v3/"
        self.keys=OAuth1(cred["wc_key"],cred["wc_sec"])

    def post(self,endpoint,payload,headers=None,expected_statuscode=200):
        self.url=self.baseurl+endpoint
        if not headers:
            headers={"Content-type":"application/json"}
        logger.info("Initiating post request")
        act_resp=requests.post(url=self.url,data=json.dumps(payload),headers=headers,auth=self.keys)
        assert act_resp.status_code == expected_statuscode,"Expected is {} but actual is {}".format(expected_statuscode,act_resp.status_code)
        return act_resp

    def get(self,endpoint,payload=None,headers=None,expected_status_code=200):
        self.url=self.baseurl+endpoint
        if not headers:
            headers={"Content-type":"application/json"}
        logger.debug("Initiating get request")
        act_resp=requests.get(url=self.url,headers=headers,payload=payload,auth=self.keys)

        assert act_resp.status_code==expected_status_code,"Expected is {} but actual is {}".format(expected_status_code,act_resp.status_code)
        return act_resp




