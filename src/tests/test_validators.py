import pytest


class TestValidateIsInt:

    def get_target(self):
        from validators import validate_is_int
        return validate_is_int

    def test_valid(self):
        fn = self.get_target()
        assert fn(1) is True

    def test_invalid(self):
        fn = self.get_target()
        assert fn('a') is False


class TestValidateIsStr:

    def get_target(self):
        from validators import validate_is_str
        return validate_is_str

    @pytest.mark.parametrize('a,expected', [
        ('a', True),
        ('あ', True),
        (1, False),
        (object(), False),
        (None, False),
        (False, False),
    ])
    def test_str(self, a, expected):
        fn = self.get_target()
        assert fn(a) is expected
