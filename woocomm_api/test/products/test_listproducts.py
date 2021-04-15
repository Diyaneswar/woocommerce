from woocomm_api.src.utilities.request_utility import Request_Utility
import pytest
import logging as logger
from woocomm_api.src.dao.productdao import Productdao
from woocomm_api.src.helper.product_helper import Product_help

@pytest.mark.products
@pytest.mark.tcid004
def test_get_all_products():
    logger.info("*******Test case to list all products******* ")
    prd=Request_Utility()
    endpoint="products"
    prd_list=prd.get(endpoint=endpoint,expected_status_code=200)
    import pdb;pdb.set_trace()
    assert prd_list is not None,"Wrong status code"
    return prd_list

@pytest.mark.products
@pytest.mark.tcid005
def test_get_prd_by_id():
    logger.info("*******Get product list by id******* ")
    #Get a product from dao
    da_prd=Productdao().get_random_prd()
    ran_prd=da_prd[0]["ID"]


    #Initiating the get call
    prd_id = Product_help()
    prd_help=prd_id.get_product_by_id(ran_prd)

    import pdb;pdb.set_trace()
    #verify the product
