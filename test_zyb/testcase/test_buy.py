from test_zyb.page import mypages
from test_zyb.page.App import App
import pytest


class TestBuy(object):
    @classmethod
    def setup_class(cls):
        cls.jypage = App.main().gotoMypage().Joinpages().Khdmjoin("1300022253", "123321")

    # def test_buyag(self):
    #     sellpage = self.jypage.Jypage().Clickbuy()
    #     sellpage.Buygp("000001")
    #     #self.jypage.Jypage().Clickbuy().Buygp(self, "600001", "1000")
    #     assert "委托请求发送成功" in sellpage.getSucceed()

    @pytest.mark.parametrize("gpdm, num",
                             [('000001', 100),
                              ("600001", 200),
                              ("159001", 300),
                             ])
    def test_buyag(self, gpdm, num):
        sellpage = self.jypage.Jypage().Clickbuy()
        sellpage.Buygp(gpdm, num)
        #self.jypage.Jypage().Clickbuy().Buygp(self, "600001", "1000")
        assert "委托请求发送成功" in sellpage.getSucceed()