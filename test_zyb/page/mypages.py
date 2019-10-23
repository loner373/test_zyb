from selenium.webdriver.common.by import By

from test_zyb.driver.AndroidClient import AndroidClient
from test_zyb.page.BasePage import BasePage
from test_zyb.page.jypage import JYpage

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

        jy = (By.XPATH, "//*[@text='交易'and @instance='2']")
        self.find(jy).click()
        return JYpage()