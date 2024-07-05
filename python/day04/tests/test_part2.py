import pytest

from part2 import is_valid


@pytest.mark.parametrize(
    "passphrases,expected",
    [
        ("abcde fghij", True),
        ("abcde xyz ecdab", False),
        ("a ab abc abd abf abj", True),
        ("iiii oiii ooii oooi oooo", True),
        ("oiii ioii iioi iiio", False),
    ],
    ids=[
        "abcde fghij_should_be_True",
        "abcde xyz ecdab_should_be_False",
        "a ab abc abd abf abj_should_be_True",
        "iiii oiii ooii oooi oooo_should_be_True",
        "oiii ioii iioi iiio_should_be_False",

    ],
)
def test_part1(passphrases: str, expected: int) -> None:
    result: int = is_valid(passphrases)
    assert result == expected, f"got {result}, needs {expected}"
