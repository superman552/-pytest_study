import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWeb():
    def setup_class(self):
        #浏览器复用：1.将Chrome的启动文件添加到环境变量，2.执行命令chrome --remote-debugging-port=9222
        #注意需要把其他谷歌浏览器关掉。
        # """
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(chrome_options=options)
        # """
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    def test_02(self):
        """使用cookie实现扫码免登陆"""
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)

    def test_01(self):
        """使用cookie实现扫码免登陆"""
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)

        # cookies = self.driver.get_cookies()
        # print(cookies)
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        # self.driver.refresh()
        cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
          'value': 'N_KwNnaJLPZjQVDAVQFbXJzPKsMSH0dymNfJ6dSWuKHTyqqdfNzs2m-dB_iofwwQ'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
          'value': 'a1613720'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
          'value': '1688850000710676'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
          'value': 'EOxk4vHr3MMaVT56etTa2AStiSAqDS3uYLUDB6GHyJaYU1nn7SzDMmNKPn5pa4Of8SD_KeHFS9rwar0mDOUAh6235R5T1pqU37HTi1CgF_OMRUeg8_S1Qx72HG5xdfKCMMJtUeQ6N1BMzpNoY-sIeIFTF7EYYvh2GsF4tOmD9wM5BmnKPf55bjdsjNhwUOOvxNh2frwI2mmt6OZIJgiHI-HE7Qpm-KTBi-0xxMrpK4vmEzeAngCYvMilU1XliG4b403acxULjBLkP4zMNqqZ5A'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
          'value': '1970324973164711'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
          'value': '1688850000710676'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
          'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1634967752, 'httpOnly': False,
                          'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                          'value': '1603430337,1603431753'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
          'value': 'direct'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
          'path': '/', 'secure': False, 'value': '1603431753'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
          'value': '0246689'},
         {'domain': '.qq.com', 'expiry': 1603518437, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
          'value': 'GA1.2.850709041.1603430337'},
         {'domain': 'work.weixin.qq.com', 'expiry': 1603461871.78784, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
          'secure': False, 'value': '6alhc6d'},
         {'domain': '.qq.com', 'expiry': 1666504037, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
          'value': 'GA1.2.1026998543.1603430337'},
         {'domain': '.work.weixin.qq.com', 'expiry': 1634966335.787879, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
          'path': '/', 'secure': False, 'value': '0'},
         {'domain': '.work.weixin.qq.com', 'expiry': 1606024090.261155, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
          'path': '/', 'secure': False, 'value': 'zh'}]
        #将cookie持久化
        cookies_shelve = shelve.open('shelve')
        cookies_shelve['cookiesadd'] = cookies
        cookies_shelve.close()
        cookies_shelve = shelve.open('shelve')
        cookies_she=cookies_shelve['cookiesadd']
        cookies_shelve.close()

        for cookie in cookies_she:
            self.driver.add_cookie(cookie)
        sleep(2)
        self.driver.refresh()
        sleep(2)

    def test_fileup(self):
        self.driver.find_element_by_xpath('//*[@class="index_service_cnt js_service_list"]//a[2]').click()
        sleep(2)
        self.driver.find_element_by_css_selector('.ww_fileImporter_fileContainer_uploadInputMask').send_keys('C:\\Users\\Admin\\Desktop\\111.xls')
        sleep(3)
        res = self.driver.find_element_by_css_selector('.ww_fileImporter_fileContainer_fileNames').get_attribute("innerHTML")
        sleep(3)
        print("*********"+res+"**********")
        assert res == "111.xls"




