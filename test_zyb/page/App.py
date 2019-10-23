from test_zyb.driver.AndroidClient import AndroidClient
from test_zyb.page.mainpages import Mainpage


class App(object):
    @classmethod
    def main(self):
        AndroidClient.installApp()
        return Mainpage()
