# 被测代码 ，计算器（加 减 乘 除）

class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            print("被除数不能为0")
            return False

    # div.index_service_cnt.js_service_list > a: nth - child(2)
    # .index_service_cnt
    # js_service_list
    # a: nth - child(2)