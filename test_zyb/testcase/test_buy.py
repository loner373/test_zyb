from test_zyb.page.mainpages import Mainpage

import pytest

class TestBuy(object):
    def test_buyag(self):
        main = Mainpage()
        main.gotoMypage().Joinpage().Joinpage()
