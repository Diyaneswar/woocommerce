import pytest
import logging as logger
from woocomm_api.src.utilities.generic_utility import email_and_passgen
from woocomm_api.src.helper.customer_helper import Customer_help
from woocomm_api.src.dao.customerdao import Get_customer_byemail
from woocomm_api.src.utilities.request_utility import Request_Utility

@pytest.mark.customers
@pytest.mark.tcid001
def test_create_customer_tcid001():
    logger.info("Test case to create a customer with email and password")
    #email and password generation
    randinfo = email_and_passgen()
    email = randinfo["email"]
    password = randinfo["password"]

    cust_obj=Customer_help()
    cust_resp=cust_obj.create_customer(email,password)

    #verfiying email from API response
    assert cust_resp["email"]==email,"Email not created successfully"

    #verifying email generated in db
    email_indb=Get_customer_byemail()
    rs_sql=email_indb.get_cust_by_email(cust_resp["email"])

    assert cust_resp['id']==rs_sql[0]['ID'],"email not generated in db successful"

@pytest.mark.customers
@pytest.mark.tcid003
def test_check_email_exists():#negative test case
    logger.info("********Test case to check email already exists********")
    rand=Get_customer_byemail()
    rand_user_list=rand.get_cust_random_email()
    rand_email=rand_user_list[0]["user_email"]

    req=Request_Utility()
    payload={"email":rand_email}
    resp=req.post(endpoint="customers",payload=payload,expected_statuscode=400)

    assert resp.json()["code"]=='registration-error-email-exists'
    assert resp.json()["message"]=='An account is already registered with your email address. ' \
                                   '<a href="#" class="showlogin">Please log in.</a>'





