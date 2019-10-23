from test_zyb.page import  mypages
from test_zyb.page.App import App
import pytest

class TestBuy(object):
    @classmethod
    def setup_class(cls):
        cls.jypage=App.main().gotoMypage().Joinpages().Join()
    def test_buyag(self):
        self.jypage.Jypage().Clickbuy().Buygp(["xpath", "gp"], ["xpath", "numbe"])
        assert self.jypage.Weituo().Nmae()=="gp"






