from app_study.popages.appbase import AppBase


class TestAddContact:
    def setup_class(self):
        self.appbase = AppBase()
    def test_addcontact(self):
        name = '李四'
        gender = '男'
        phonenum = '18956235689'
        self.appbase.start().goto_main().goto_contactpage().goto_addcontactpage().goto_contacteditpage().contactedit(name, gender, phonenum)

