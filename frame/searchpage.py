from selenium.webdriver.common.by import By

from frame.base_page import BasePage


class SearchPage(BasePage):
    def input_send(self):
        self.find(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')