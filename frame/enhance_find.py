from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import allure
# def enhance_find(func):
#     black_lists = [(By.ID, 'com.xueqiu.android:id/iv_close1')]
#     def wrapper(*args, **kwargs):
#         from frame.base_page import BasePage
#         instance: BasePage = args[0]
#         for i in [1,4]:
#             try:
#                 res = func(*args, **kwargs)
#                 return res
#             except Exception as e:
#                 for black_list in black_lists:
#                     for ele in instance.driver.find_elements(*black_list):
#                         ele.click()
#         raise e
#     return wrapper





def enhance_find(func):
    # @wraps(f)#加上该装饰器，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。
    # print(f.__name__)
    def wrapper(*args, **kwargs):#*args, **kwargs能接收到func的参数。
        from frame.base_page import BasePage
        instance: BasePage = args[0]
        # instance = BasePage()
        try:
            result = func(*args, **kwargs)
            instance.err_num = 0
            return result
        except Exception as e:
            instance.driver.save_screenshot('tmp.png')
            with open('tmp.png','rb') as f:
                content = f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            if instance.err_num > instance.max_num:
                raise e
            instance.err_num += 1
            # 从黑名单中遍历元素，依次进行处理
            for black_ele in instance.black_list:
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    # 处理完黑名单后，再次查找原来的元素
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper















