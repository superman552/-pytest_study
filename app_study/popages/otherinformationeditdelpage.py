from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_study.popages.basepage import BasePage


class OtherInformationEditDelPage(BasePage):
    def del_contact(self):
        # sleep(3)
        WebDriverWait(self.driver,10).until(lambda x:x.find_element(MobileBy.XPATH,'//*[@text="删除成员"]'))
        self.roll_find("删除成员").click()
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,'//*[@text="确定"]'))).click()
        return True

