from selenium.webdriver.common.by import By

from app_study.popages.basepage import BasePage
from app_study.popages.contactpage import ContactPage


class MainPage(BasePage):
    def goto_contactpage(self):
        """点击计入通讯录"""
        self.driver.find_element(By.XPATH, '//*[@text="通讯录"]').click()
        return ContactPage(self.driver)

