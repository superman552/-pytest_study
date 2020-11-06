from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app_study.popages.basepage import BasePage


class ContactEditPage(BasePage):
    def contactedit(self,name, gender, phonenum):
        # 设置 【用户名】【性别】【手机号】
        self.driver.find_element(MobileBy.XPATH,
                  "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()

        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH,
                  '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//android.widget.EditText').send_keys(
            phonenum)
        # 点击【保存】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        from app_study.popages.addcontactpage import AddContactPage
        # return AddContactPage(self.driver)
        return True

