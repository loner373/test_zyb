from test_zyb.page.BasePage import BasePage
from test_zyb.page.mainpages import Mainpage


class TestLogin(BasePage):
    def test_login(self):
        login= Mainpage.gotoMypage().Joinpages().Khdmjoin()