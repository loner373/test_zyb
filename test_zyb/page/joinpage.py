from selenium.webdriver.common.by import By

from test_zyb.driver.AndroidClient import AndroidClient
from test_zyb.page.BasePage import BasePage
from test_zyb.page.mypages import Mypage

class Joinpage(BasePage):
    def Khdmjoin(self):
        #todo:登录完成
        account = (By.ID, "edit_account")
        self.find(account)
        self.find(account).send_keys("130002253")
        passwped = (By.ID, "edit_password")
        self.find(passwped).click()
        self.find(passwped).send_keys("123321")
        dl = (By.ID, "edit_yanzhengma")
        self.find(dl)
        self.find(dl).click()
        yzm = (By.ID, "edit_yanzhengma")
        self.find(yzm).send_keys("8888")
        login = (By.ID, "login")
        self.find(login)
        self.find(login).click()
        return Mypage()
    def Zjdmjoin(self):
        #todo:
        return self


