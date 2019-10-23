from appium.webdriver import WebElement

from test_zyb.driver.AndroidClient import AndroidClient


class BasePage():
    def __init__(self):
        self.driver=AndroidClient.driver

    def find(self, kv) -> WebElement:
        self.driver.find_element(*kv)
