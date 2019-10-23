from selenium.webdriver.common.by import By

from test_zyb.page.BasePage import BasePage
from test_zyb.page.jypage import JYpage
from test_zyb.page.wtpages import WTpage


class Mypage(BasePage):

    def Joinpages(self):
        denglu = (By.ID, "立即登录")
        self.find(denglu).click()
        from test_zyb.page.joinpage import Joinpage
        return Joinpage()
    def Getnumber(self):

        #todo:
        return self
    def Jypage(self):

        #jy = (By.XPATH, "//*[@text='交易'and @instance='2']")
        jy = "交易"
        self.findByText(jy)
        self.findByText(jy).click()
        return JYpage()

    def Weituo(self):
        wt = "委托"
        self.findByText(wt)
        self.findByText(wt).click()
        return WTpage()

