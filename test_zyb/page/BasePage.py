from test_zyb.driver.AndroidClient import AndroidClient


class BasePage():
    def __init__(self):
        self.driver=AndroidClient.driver