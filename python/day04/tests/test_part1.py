import pytest

from part1 import is_valid


@pytest.mark.parametrize(
    "passphrases,expected",
    [
        ("aa bb cc dd ee", True),
        ("aa bb cc dd aa", False),
        ("aa bb cc dd aaa", True),
    ],
    ids=[
        "aa bb cc dd ee should_be_True",
        "aa bb cc dd aa should_be_False",
        "aa bb cc dd aaa should_be_True",
    ],
)
def test_part1(passphrases: str, expected: int) -> None:
    result: int = is_valid(passphrases)
    assert result == expected, f"got {result}, needs {expected}"
