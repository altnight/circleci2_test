from typing import Any


def validate_is_int(a: Any) -> bool:
    if not isinstance(a, int):
        return False
    return True


def validate_is_str(a: Any) -> bool:
    if not isinstance(a, str):
        return False
    return True
