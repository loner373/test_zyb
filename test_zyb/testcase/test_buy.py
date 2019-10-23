from test_zyb.page.mainpages import Mainpage
from test_zyb.page.App import App
import pytest

class TestBuy(object):
    def test_buyag(self):
        App.main().gotoMypage().Joinpages().Join()
