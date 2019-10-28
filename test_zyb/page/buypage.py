from selenium.webdriver.common.by import By

from test_zyb.page.BasePage import BasePage



class Buypage(BasePage):
    _gp = (By.ID, "tzt_trade_edit_stockcode")
    _num = (By.ID, "tzt_trade_linear_count_addcount_icon")
    _Qued1 = (By.XPATH, "//*[@text='立即买入']")
    _Qued2 = (By.XPATH, "//*[@text='买入']")
    _text = (By.XPATH, "//*[@text='确定']/../..//*[@instance=2]//*[@instance=1]")
    _Qued3 = (By.XPATH, "//*[@text='确定']")
    def Buygp(self, gpdm):
        #todo:
        #股票
        self.find(self._gp).click()
        self.find(self._gp).send_keys(gpdm)
        #数量
        self.find(self._num).click()
        #self.find(self._num).send_keys(numbe)
        #self.find(Qued1)
        self.find(self._Qued1).click()
        #self.find(Qued2)
        self.find(self._Qued2).click()

        return Buypage()
    def getSucceed(self):
        msg = self.find(self._text).text
        self.find(self._Qued3).click()
        return msg


