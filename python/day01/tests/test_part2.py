import pytest

from part2 import solve


@pytest.mark.parametrize(
    "input,expected",
    [
        ("1212", 6),
        ("1221", 0),
        ("123425", 4),
        ("123123", 12),
        ("12131415", 4),
    ],
    ids=[
        "1212_should_be_6",
        "1221_should_be_0",
        "123425_should_be_4",
        "123123_should_be_12",
        "12131415_should_be_4",
    ],
)
def test_solve(input: str, expected: int) -> None:
    result: int = solve(input)
    assert result == expected, f"got {result}, needs {expected}"
