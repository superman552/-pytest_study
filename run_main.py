import time
import pytest
import os
import sys

sys.path.extend('.')


# def del_files(path):
#   for root , dirs, files in os.walk(path):
#     for name in files:
#       if name.endswith("result.json") or name.endswith(".txt"):   #指定要删除的格式，这里是jpg 可以换成其他格式
#         os.remove(os.path.join(root, name))
#         print ("Delete File: " + os.path.join(root, name))

if __name__ == '__main__':
    # path = '.\\results'
    # del_files(path)
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # pytest.main(["-sq",
    #              "--alluredir", "results\\json{}".format(now)])
    #
    # os.system("allure generate D:\\allure_study\\results\\json{} -o report\\html{}".format(now,now))
    pytest.main(["-sq","--alluredir", "results"])

    # os.system("allure generate .\\results -o report\\html{}".format(now))