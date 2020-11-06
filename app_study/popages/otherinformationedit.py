from appium.webdriver.common.mobileby import MobileBy

from app_study.popages.basepage import BasePage
from app_study.popages.otherinformationeditdelpage import OtherInformationEditDelPage


class OtherInformationEditPage(BasePage):
    def goto_edit_del_page(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="编辑成员"]').click()
        return OtherInformationEditDelPage(self.driver)