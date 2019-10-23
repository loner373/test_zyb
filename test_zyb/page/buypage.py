from selenium.webdriver.common.by import By

from test_zyb.page.BasePage import BasePage



class Buypage(BasePage):
    def Buygp(self, gpdm, numbe):
        #todo:
        self.Click(*gpdm)
        self.Click(*numbe)
        Qued1 = (By.XPATH, " ")
        self.find(Qued1)
        self.find(Qued1).click()
        Qued2 = (By.XPATH, " ")
        self.find(Qued2).click()
        return self

