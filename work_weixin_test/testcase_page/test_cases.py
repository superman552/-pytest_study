from work_weixin_test.popage.mainpage import MainPage


class TestCases:
    # def setup(self):
    mainpage = MainPage()

    def test_inaddmember(self):
        # self.mainpage.get()
        self.mainpage.gote_addmemberpage_click()
        self.mainpage.gote_addmemberpage().addmember()
        self.mainpage.gote_addmemberpage().get_name_list()




