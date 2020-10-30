from time import sleep

from work_weixin_test.popage.basepage import BasePage


class AddmemberPage(BasePage):
    def addmember(self):
        username= 'aaaa'
        account = '123456'
        phonenum = '18565656565'
        self.driver.find_element_by_css_selector('#username').send_keys(username)
        sleep(3)
        self.driver.find_element_by_css_selector('#memberAdd_acctid').send_keys(account)
        sleep(3)
        self.driver.find_element_by_css_selector('.ww_telInput_mainNumber').send_keys(phonenum)
        sleep(3)
        self.driver.find_element_by_css_selector('.js_member_editor_form>div:nth-child(1) a:nth-child(2)').click()

    def get_name_list(self):
        eles = self.driver.find_elements_by_css_selector('.js_list .member_colRight_memberTable_td:nth-child(2)')
        sleep(3)
        name_list = [element.get_attribute('title') for element in eles]
        print(name_list)
        return name_list
