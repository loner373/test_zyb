from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from appium import webdriver


class AndroidClient(object):
    driver : WebDriver
    @classmethod
    #直接启动
    def installApp(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "huawei"
        caps["appPackage"] = "com.ytsc"
        caps["appActivity"] = "com.zztzt.android.simple.activity.tztCommHeadPageActivity"
        #caps["autoGrantPermissions"] = "true"
        caps["noReset"] = True
        caps["unicodeKeyboard"]=True
        caps["resetKeyboard"]=True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver
    #重新安装
    def restartApp(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "huawei"
        caps["appPackage"] = "com.ytsc"
        caps["appActivity"] = "com.zztzt.android.simple.activity.tztCommHeadPageActivity"
        caps["autoGrantPermissions"] = "true"
        #caps["noReset"] = True
        caps["fullReset"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver
        return self
