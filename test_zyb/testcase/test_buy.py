from test_zyb.page import mypages
from test_zyb.page.App import App
import pytest


class TestBuy(object):
    @classmethod
    def setup_class(cls):
        cls.jypage = App.main().gotoMypage().Joinpages().Khdmjoin("1300022253", "123321")

    def test_buyag(self):
        self.jypage.Jypage().Clickbuy().Buygp("000001")
        #self.jypage.Jypage().Clickbuy().Buygp(self, "600001", "1000")
        assert "委托请求发送成功" in self.jypage.Jypage().Clickbuy().getSucceed()

   # @pytest.mark.parametrize("gpdm, numbe" [
   #                         "000001", "1000"
   #                          ])
    #def test_buyag(self, gpdm, numbe):
    #    self.jypage.Jypage().Clickbuy().Buygp("gpdm", "numbe")
    #    assert self.jypage.Weituo().Nmae() == "gpdm"
