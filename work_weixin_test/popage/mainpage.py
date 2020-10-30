from work_weixin_test.popage.addmemberpage import AddmemberPage
from work_weixin_test.popage.basepage import BasePage


class MainPage(BasePage):

    def get(self):
        self.driver.get("https://www.baidu.com")
    def gote_addmemberpage_click(self):
        self.driver.find_element_by_css_selector('.js_service_list a:nth-child(1) span:nth-child(2)').click()
    #     .js_has_member>div:nth-child(1)>a:nth-child(2)

    def gote_addmemberpage(self):
        return AddmemberPage(self.driver)
