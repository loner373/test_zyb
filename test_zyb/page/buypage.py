from selenium.webdriver.common.by import By

from test_zyb.page.BasePage import BasePage

import time

class Buypage(BasePage):
    _gp = (By.ID, "tzt_trade_edit_stockcode")
    _num = (By.XPATH, "//*[contains(@class,'android.widget.EditText')and@instance=2]")
    _Qued1 = (By.XPATH, "//*[@text='立即买入']")
    _Qued2 = (By.XPATH, "//*[@text='买入']")
    _text = (By.XPATH, "//*[@text='确定']/../..//*[@instance=2]//*[@instance=1]")
    _Qued3 = (By.XPATH, "//*[@text='确定']")
    _back = (By.XPATH,"//*[contains(@class,'android.widget.Button')and@instance=0]")
    def Buygp(self, gpdm, num):
        #todo:
        #股票
        self.find(self._gp).click()
        self.find(self._gp).send_keys(gpdm)
        time.sleep(3)
        #数量
        self.find(self._num).click()
        self.find(self._num).send_keys(num)
        #self.find(Qued1)
        self.find(self._Qued1).click()
        #self.find(Qued2)
        self.find(self._Qued2).click()

        return Buypage()
    def getSucceed(self):
        msg = self.find(self._text).text
        self.find(self._Qued3).click()
        self.find(self._back).click()
        return msg


