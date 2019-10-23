from test_zyb.driver.AndroidClient import AndroidClient
from test_zyb.page.BasePage import BasePage
from test_zyb.page.mypages import Mypage


class Mainpage(BasePage):


    def gotoMypage(self):

        self.driver.find_element_by_xpath("//*[@text='我的'and @instance='5']")
        self.driver.find_element_by_xpath("//*[@text='我的'and @instance='5']").click()
        return Mypage()