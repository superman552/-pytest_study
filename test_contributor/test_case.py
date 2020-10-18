import pytest
from python_code.contributor import Calculator


class TestCalc:
    def setup(self):
        print("计算开始")
        self.cal = Calculator()

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a, b,res', [[5, 3, 2], [0.9, 0.8, 0.1], [-3, -4, 1]],
                             ids=['intcase', 'floatcase', 'minuscase'])
    def test_sub(self, a, b, res):
        assert self.cal.sub(a, b) == res

    @pytest.mark.parametrize('a, b, res', [[3, 3, 9], [0.5, 0.5, 0.25], [-3, -5, 15]])
    def test_mul(self, a, b, res):
        assert self.cal.mul(a, b) == res

    @pytest.mark.parametrize('a, b, res', [[20, 4, 5], [0.5, 0.5, 1], [15, -5, -3], [2, 0, False]])
    def test_div(self, a, b, res):
        assert self.cal.div(a, b) == res
