import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver



class BasePage:
    def __init__(self, driver:WebDriver=None):
        self.driver = driver


    def roll_find(self,text):
        """
        滚动查找元素方法
        :param text: 查找的文本内容
        :return:元素
        """
        ele = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

        return ele


