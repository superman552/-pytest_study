#基类
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver = None):
        # self.driver = driver
        if driver == None:
            # self.driver = webdriver.Chrome()
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(chrome_options=options)
            # self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            # self.driver.maximize_window()
        else:
            self.driver = driver
        # return driver

    def test_01(self):
        """使用cookie实现扫码免登陆"""
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
    # def find_element_clickable(self,):
    #     pass

