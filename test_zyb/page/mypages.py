from test_zyb.driver.AndroidClient import AndroidClient
from test_zyb.page.BasePage import BasePage
from test_zyb.page.jypage import JYpage

class Mypage(BasePage):

    def Joinpages(self):

        self.driver.find_element_by_id("立即登录")
        self.driver.find_element_by_id("立即登录").click()
        from test_zyb.page.joinpage import Joinpage
        return Joinpage()
    def Getnumber(self):
        #todo:
        return self
    def Jypage(self):

        self.driver.find_element_by_xpath("//*[@text='交易'and @instance='2']")
        self.driver.find_element_by_xpath("//*[@text='交易'and @instance='2']").click()
        return JYpage()