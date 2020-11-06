from appium.webdriver.common.mobileby import MobileBy

from app_study.popages.basepage import BasePage
from app_study.popages.otherinformationedit import OtherInformationEditPage


class OtherInformationPage(BasePage):
    def goto_otherinformationeditpage(self):
        #点击右上方三个点，进入个人信息编辑页面
        self.driver.find_element(MobileBy.XPATH,'//android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView').click()
        return OtherInformationEditPage(self.driver)
