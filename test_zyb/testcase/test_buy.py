from test_zyb.page.mainpage import Mainpage

import pytest

class TestBuy(object):
    def test_buyag(self):
        main=Mainpage()
        assert main.gotoMypage().Clickjoin().Join("1300022253","123321").Clickbuy().BuyAg("000001")=="确定"
