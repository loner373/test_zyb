from test_zyb.driver.AndroidClient import AndroidClient
from test_zyb.page.joinpage import Joinpage
from test_zyb.page.jypage import JYpage


class Mypage(object):
    def Joinpage(self):

        AndroidClient().driver.find_element_by_id("立即登录")
        AndroidClient().driver.find_element_by_id("立即登录").click()
        return Joinpage()
    def Jypage(self):

        AndroidClient.driver.find_element_by_xpath("//*[@text='交易'and @instance='2']")
        AndroidClient.driver.find_element_by_xpath("//*[@text='交易'and @instance='2']").click()
        return JYpage()