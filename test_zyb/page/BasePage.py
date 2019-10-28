from appium.webdriver import WebElement
from selenium.webdriver.common.by import By

from test_zyb.driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):
        self.driver = AndroidClient.driver

    def find(self, kv) -> WebElement:
        #todo：处理弹框
        return self.driver.find_element(*kv)

    def findByText(self, text ) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" %text ))

    # def Click(self, xpath, figure):
    #     self.findByText(xpath)
    #     self.findByText(xpath).click()
    #     self.findByText(xpath).send_keys(figure)
