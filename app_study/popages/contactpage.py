from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app_study.popages.addcontactpage import AddContactPage
from app_study.popages.basepage import BasePage
from app_study.popages.otherinformation import OtherInformationPage


class ContactPage(BasePage):
    def goto_addcontactpage(self):
        self.driver.find_element(By.XPATH, '//*[@text="添加成员"]').click()
        return AddContactPage(self.driver)

    def goto_otherinformationpage(self,text):
        self.driver.find_element(MobileBy.XPATH,'//android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.'
                                                'widget.LinearLayout[2]/android.widget.RelativeLayout[1]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"搜索")]').send_keys(f"{text}")

        WebDriverWait(self.driver,5).until(lambda x: x.find_element(MobileBy.XPATH,f'//*[@text="联系人"]/../..//*[@text="{text}"]'))
        self.driver.find_element(MobileBy.XPATH, f'//*[@text="联系人"]/../..//*[@text="{text}"]').click()
        return OtherInformationPage(self.driver)
