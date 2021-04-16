from woocomm_api.src.utilities.generic_utility import create_randomsring
from woocomm_api.src.utilities.request_utility import Request_Utility
from woocomm_api.src.dao.productdao import Productdao
import pytest

@pytest.mark.products
@pytest.mark.tcid006
def test_create_product():
    #generate payload
    payload={}
    payload['name']=create_randomsring(10)
    payload['type']="sample"
    payload['regular_price']="100"
    #make call
    create_prd_resp=Request_Utility().post(endpoint='products',payload=payload,expected_statuscode=201)

    #verify the response is not empty
    assert create_prd_resp,"Created product api response is empty"
    assert create_prd_resp['name']==payload['name'],"Wrong product is created"

    #verify the same created in database
    db_prod=Productdao().create_product_call(payload['ID'])
    assert db_prod[0]["name"]==payload["name"],"Product not created in the database"
