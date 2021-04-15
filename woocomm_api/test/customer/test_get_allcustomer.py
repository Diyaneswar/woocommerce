import pytest
import logging as logger
from woocomm_api.src.utilities.request_utility import Request_Utility

@pytest.mark.customers
@pytest.mark.tcid002
def test_list_all_cutomer_tcid002():
    logger.info("********testcase-To list all customers********")
    headers = {"Content-Type": "application/json"}
    req=Request_Utility()
    resp=req.get(endpoint="customers",expected_status_code=200,headers=headers)

    assert resp is not None,"There is no customers"

