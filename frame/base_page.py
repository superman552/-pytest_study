import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from frame.enhance_find import enhance_find


class BasePage:
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0
    # black_list = [(By.ID, 'com.xueqiu.android:id/iv_close')]
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            caps = {
                "platformName":"Android",
                "appPackage":"com.xueqiu.android",
                "appActivity":".view.WelcomeActivityAlias",
                "noReset":"true"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    # find=enhance_find(find)
    # find相当于已经通过调用enhance_find(find)将函数改造了，并将原始的fing函数复制给了func。而enhance_find函数返回wrapper，
    # 因此func函数和wrapper一样的了，因此调用find()就等于调用wrapper（)
    # find(self,by,value=None)就想self,by,value=None参数给了*args, **kwargs。
    @enhance_find
    def find(self,by,value=None):
        if value == None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by,value)

    def parse_yaml(self, path, func_name):
        """
        将页面步骤封装到yml文件中
        :param path: 需要解析的yml文件路径
        :param func_name: yml文件内的顶级标题
        :return:
        """
        with open(path, encoding='UTF-8') as f:
            datas = yaml.safe_load(f)
            # print(datas[func_name])
            self.parse(datas[func_name])

    def parse(self, steps):
        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'], step['value']).click()
            elif 'send_keys' == step['action']:
                self.find(step['by'], step['value']).send_keys(step['content'])
