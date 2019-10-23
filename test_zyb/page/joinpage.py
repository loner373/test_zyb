from test_zyb.driver.AndroidClient import AndroidClient
from test_zyb.page.BasePage import BasePage
from test_zyb.page.mypages import Mypage

class Joinpage(BasePage):
    def Join(self):
        #todo:登录完成
        self.driver.find_element_by_id("edit_account")
        self.driver.find_element_by_id("edit_account").click()
        self.driver.find_element_by_id("edit_account").send_keys("1300022253")
        self.driver.find_element_by_id("edit_password")
        self.driver.find_element_by_id("edit_password").click()
        self.driver.find_element_by_id("edit_password").send_keys("123321")
        self.driver.find_element_by_id("edit_yanzhengma")
        self.driver.find_element_by_id("edit_yanzhengma").click()
        self.driver.find_element_by_id("edit_yanzhengma").send_keys("8888")
        self.driver.find_element_by_id("login")
        self.driver.find_element_by_id("login").click()
        return Mypage()
