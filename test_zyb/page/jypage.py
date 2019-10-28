from selenium.webdriver.common.by import By

from test_zyb.page.BasePage import BasePage
from test_zyb.page.buypage import Buypage


class JYpage(BasePage):
    _buy= (By.ID, "买入")
    def Clickbuy(self):
        self.find(self._buy).click()
        return Buypage()
    def Clicksall(self):
        #todo:
        return Sellpage()
