from selenium.webdriver.common.by import By

from frame.base_page import BasePage
from frame.maketpage import MaketPage


class MainPage(BasePage):
    def goto_maketpage(self):
        self.parse_yaml("./main.yml","goto_maket")
        return MaketPage(self.driver)



