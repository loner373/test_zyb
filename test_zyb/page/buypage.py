from selenium.webdriver.common.by import By

from test_zyb.page.BasePage import BasePage



class Buypage(BasePage):
    def Buygp(self, gpdm, numbe):
        #todo:
        #股票
        gp = (By.XPATH, " ")
        self.find(gp)
        self.find(gp).click()
        self.find(gp).send_keys(gpdm)
        #数量
        num = (By.XPATH, " ")
        self.find(num)
        self.find(num).click()
        self.find(gp).send_keys(numbe)
        Qued1 = (By.XPATH, " ")
        self.find(Qued1)
        self.find(Qued1).click()
        Qued2 = (By.XPATH, " ")
        self.find(Qued2)
        self.find(Qued2).click()
        return self

