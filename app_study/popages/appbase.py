from appium import webdriver

from app_study.popages.basepage import BasePage
from app_study.popages.mainpage import MainPage
from app_study.yml_read import caps_yml_read

# with open('../configs/caps.yml') as f:
#     capsconfig = yaml.safe_load(f)
#     caps = capsconfig['desirecaps']
#     ip = capsconfig['server']['ip']
#     port = capsconfig['server']['port']



class AppBase(BasePage):
    def start(self):

        # caps = {
        #     "platformName": "Android",
        #     "deviceName": "127.0.0.1:7555",
        #     "noReset": "True",
        #     "appPackage": "com.tencent.wework",
        #     "appActivity": ".launch.WwMainActivity"
        # }
        # self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        caps = caps_yml_read()[0]
        ip = caps_yml_read()[1]
        port = caps_yml_read()[2]
        self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)
        self.driver.implicitly_wait(10)
        return self


    def close(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
    def goto_main(self)->MainPage:
        return MainPage(self.driver)

if __name__ == '__main__':
    a = AppBase()
    a.start()
    a.close()