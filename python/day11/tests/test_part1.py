import pytest

from part1 import solve


@pytest.mark.parametrize(
    "directions,expected",
    [
        (["ne","ne","ne"], 3),
        (["ne","ne","sw","sw"], 0),
        (["ne","ne","s","s"], 2),
        (["se","sw","se","sw","sw"], 3),
    ],
    ids=[
        '["ne","ne","ne"]_should_be_3',
        '["ne","ne","sw","sw"]_should_be_0',
        '["ne","ne","s","s"]_should_be_2',
        '["se","sw","se","sw","sw"]_should_be_3',
    ],
)
def test_part1(directions: str, expected: int) -> None:
    result: int = solve(directions)
    assert result == expected, f"got {result}, needs {expected}"
