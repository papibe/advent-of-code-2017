import pytest

from part1 import solve


@pytest.mark.parametrize(
    "input,expected",
    [
        ("1122", 3),
        ("1111", 4),
        ("1234", 0),
        ("91212129", 9),
    ],
    ids=[
        "1122_should_be_3",
        "1111_should_be_4",
        "1234_should_be_0",
        "91212129_should_be_9",
    ],
)
def test_solve(input: str, expected: int) -> None:
    result: int = solve(input)
    assert result == expected, f"got {result}, needs {expected}"
