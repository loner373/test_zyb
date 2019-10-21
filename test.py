# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

class Basepage:
    caps = {}
    caps["platformName"] = "Android"
    caps["deviceName"] = "huawei"
    caps["appPackage"] = "com.ytsc"
    caps["appActivity"] = "com.zztzt.android.simple.activity.tztCommHeadPageActivity"
    caps["autoGrantPermissions"] = "true"
    #是否不重置
    #caps["noReset"] = "ture"
    #caps["fullReset"] = "ture"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    driver.implicitly_wait(10)
    driver.implicitly_wait(10)

    el1 = driver.find_element_by_id("tv_confirm")
    el1.click()
    el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.ImageView")
    el2.click()
    el3 = driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"交易\"]/android.view.View/android.widget.ListView[1]/android.view.View[1]")
    el3.click()
    el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.Button")
    el4.click()

    driver.quit()