import pytest
from datetime import datetime,timedelta
from woocomm_api.src.helper.product_helper import Product_help
from woocomm_api.src.dao.productdao import Productdao
@pytest.mark.regression
class TestListProductUsingFilter():

    @pytest.mark.tcid007
    def test_list_prd_filter_after(self):
        #create payload
        payload={}
        act_date=datetime.now().replace(microsecond=0)-timedelta(1)
        correct_date_fmt=act_date.isoformat()
        payload['after']=correct_date_fmt

        #make the get call
        prd_resp=Product_help().call_product_by_filter(payload['after'])

        #verify the response in the database
        db_resp=Productdao().get_product_using_filter(payload['after'])

        #verify len of the response is same as in the database
        assert len(db_resp)==len(prd_resp),"Wrong data fetched for the date"

        #verify the ids of the response matches in the database
        db=[i["ID"] for i in db_resp]
        act_resp=[j["ID"] for j in prd_resp]
        final=list(set(db)-set(act_resp))
        assert final,"Number of ids are not matching"

