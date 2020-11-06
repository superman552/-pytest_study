from selenium.webdriver.common.by import By

from app_study.popages.basepage import BasePage
# from app_study.popages.contacteditpage import ContactEditPage


class AddContactPage(BasePage):
    def goto_contacteditpage(self):
        self.driver.find_element(By.XPATH,'//*[@text="手动输入添加"]').click()
        from app_study.popages.contacteditpage import ContactEditPage
        return ContactEditPage(self.driver)