from selenium.webdriver.common.by import By

from frame.base_page import BasePage
from frame.searchpage import SearchPage


class MaketPage(BasePage):
    def goto_searchpage(self):
        self.find(By.ID, 'com.xueqiu.android:id/action_search').click()
        return SearchPage(self.driver)