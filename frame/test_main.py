from frame.mainpage import MainPage


class TestMain:
    def setup_class(self):
        self.main = MainPage()
    def test_main(self):
        self.main.goto_maketpage().goto_searchpage().input_send()
