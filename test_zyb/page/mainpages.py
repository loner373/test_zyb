from test_zyb.driver.AndroidClient import AndroidClient
from test_zyb.page.mypages import Mypage


class Mainpage(object):
    def __init__(self):
        AndroidClient.installApp()
    def gotoMypage(self):

        AndroidClient.driver.find_element_by_xpath("//*[@text='我的'and @instance='5']")
        AndroidClient.driver.find_element_by_xpath("//*[@text='我的'and @instance='5']").click()
        return Mypage()