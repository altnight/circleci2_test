import pytest


class TestAdd:

    def get_target(self):
        from calc import add
        return add

    def test_add_correct(self):
        fn = self.get_target()
        assert fn(1, 2) == 3

    def test_add_wrong(self):
        fn = self.get_target()
        assert not fn(1, 2) == 2


class TestMul:

    def get_target(self):
        from calc import mul
        return mul

    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 2),
        (2, 3, 6),
        (3, 6, 18),
        (6, 18, 108),
    ])
    def test_mul_correct(self, a, b, expected):
        fn = self.get_target()
        assert fn(a, b) == expected

    @pytest.mark.parametrize("a", (1, 2, 3, 6))
    @pytest.mark.parametrize("b", (1, 3, 6, 18))
    @pytest.mark.parametrize("expected", (0, 10, 19, 109))
    def test_mul_wrong(self, a, b, expected):
        fn = self.get_target()
        assert not fn(a, b) == expected
