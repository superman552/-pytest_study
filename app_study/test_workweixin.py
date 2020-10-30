#https://github.com/appium/python-client
#pip install Appium-Python-Client
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWorkWeinxin:

    def setup(self):
        caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "noReset": "True",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity"
            ""
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)

    def test_daka(self):
        self.driver.update_settings({"waitForIdleTimeout": 2})
        self.driver.find_element(By.XPATH,'//*[@text="工作台"]').click()
        #实现滚动查找元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        self.driver.find_element(By.XPATH, '//*[@text="外出打卡"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        assert WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)

    def teardown(self):
        self.driver.quit()

