import yaml

from frame.base_page import BasePage


# class Test_ll(BasePage):
# def test01():
#     path = './main.yml'
#     with open(path, encoding='UTF-8') as f:
#         datas = yaml.safe_load(f)
#         print(datas)
#         print(datas["hangqing"])
#         a = datas["hangqing"]
#         for step in a:
#             if 'click' == step['action']:
#                 print(step['action'])
#             elif 'send_keys' == step['action']:
#                 print(12)


from functools import wraps


def decorator_name(f):
    print(f(33333333))
    print(f.__name__)
    # @wraps(f)#加上该装饰器，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。
    def decorated(*args, **kwargs):
        if not can_run:
            print(args)
            # return "Function will not run"

        return f(*args, **kwargs)

    return decorated

# func=decorator_name(func)
# func()相当于已经通过调用decorator_name（func）将函数改造了，并将原始的func函数复制给了f。而decorator_name函数返回decorated，因此func函数和decorated
# 一样的了，因此调用func(111)就等于调用decorated（111)

@decorator_name
def func(a):
    print("aaaaa")
    return (a)


# can_run = True
# print(func())
# Output: Function is running

can_run = False
print(func(222))
print(func.__name__)
# Output: Function will not run