from app_study.popages.appbase import AppBase


class TestAddContact:
    def setup_class(self):
        self.appbase = AppBase()

    def test_delcontact(self):
        self.appbase.start().goto_main().goto_contactpage().goto_otherinformationpage("地点").goto_otherinformationeditpage().goto_edit_del_page().del_contact()
