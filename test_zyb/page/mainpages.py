from selenium.webdriver.common.by import By

from test_zyb.driver.AndroidClient import AndroidClient
from test_zyb.page.BasePage import BasePage
from test_zyb.page.mypages import Mypage


class Mainpage(BasePage):


    def gotoMypage(self):

        wode = (By.XPATH, "//*[@text='我的'and @instance='5']")
        self.find(wode)
        #self.driver.find_element_by_xpath("//*[@text='我的'and @instance='5']")
        #self.driver.find_element_by_xpath("//*[@text='我的'and @instance='5']").click()
        self.find(wode).click()
        return Mypage()