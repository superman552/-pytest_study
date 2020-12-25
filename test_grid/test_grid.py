from time import sleep
import allure
import pytest
from selenium import webdriver

@allure.feature("dfjk")
class TestCase:
    def setup(self):
        ds = {'platform': 'ANY',
              'browserName': "chrome",
              'version': '',
              'javascriptEnabled': True
              }
        self.dr = webdriver.Remote('http://localhost:5566/wd/hub', desired_capabilities=ds)

    def test_something(self):
        self.dr.get("https://www.baidu.com")
        sleep(10)

    def test_search_button(self):
        self.dr.get("https://www.qq.com")
        sleep(10)

    def test_search_button1(self):
        self.dr.get("https://pypi.org/project/pytest-xdist/")
        sleep(10)
    def test_search_button2(self):
        self.dr.get("https://pypi.org/project/")
        sleep(10)
    def test_search_button3(self):
        self.dr.get("https://pypi.org/")
        sleep(10)

    def teardown(self):
        self.dr.quit()


if __name__ == '__main__':
    pytest.main(["-sq","--alluredir", "results"])