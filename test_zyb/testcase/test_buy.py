from test_zyb.page import  mypages
from test_zyb.page.App import App
import pytest

class TestBuy(object):
    @classmethod
    def setup_class(cls):
        cls.jypage=App.main().gotoMypage().Joinpages().Join()
    def test_buyag(self):
        self.jypage.Jypage().Clickbuy().Buygp("000001", "1000")
        assert self.jypage.Weituo().Nmae()=="000001"
    @pytest.mark.parametrize("gpdm, numbe"[
                    ("000001", "1000")
                    ("600000", "1000")
                    ("159000", "1000")
                    ("000001", "1000")
    ])
    def test_buyag(self, gpdm, numbe):
        self.jypage.Jypage().Clickbuy().Buygp("gpdm", "numbe")
        assert self.jypage.Weituo().Nmae()=="gpdm"






