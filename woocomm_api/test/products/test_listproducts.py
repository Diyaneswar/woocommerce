from woocomm_api.src.utilities.request_utility import Request_Utility
import pytest
import logging as logger

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
def test_get_prd_by_id():
    logger.info("*******Get product list by id******* ")
    #Get a product from dao
    #Initiating the get call
    #verify the product