from selenium.webdriver.common.by import By

from test_zyb.driver.AndroidClient import AndroidClient
from test_zyb.page.BasePage import BasePage
from test_zyb.page.mypages import Mypage

class Joinpage(BasePage):
    _account = (By.ID, "edit_account")
    _passwped = (By.ID, "edit_password")
    _dl = (By.ID, "edit_yanzhengma")
    _yzm = (By.ID, "edit_yanzhengma")
    _login = (By.ID, "login")

    def Khdmjoin(self, accounts, passwords):
        #todo:登录完成
        self.find(self._account)
        self.find(self._account).send_keys(accounts)
        self.find(self._passwped).click()
        self.find(self._passwped).send_keys(passwords)
        self.find(self._dl).click()
        self.find(self._yzm).send_keys("8888")
        self.driver.implicitly_wait(10)
        self.find(self._login).click()
        return Mypage()
    def Zjdmjoin(self):
        #todo:
        return self


