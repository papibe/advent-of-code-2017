import pytest

from part2 import solve


@pytest.mark.parametrize(
    "input_,size, expected",
    [
        ("", 256, "a2582a3a0e66e6e86e3812dcb672a272"),
        ("AoC 2017", 256, "33efeb34ea91902bb2f59c9920caa6cd"),
        ("1,2,3", 256, "3efbe78a8d82f29979031a4aa0b16a9d"),
        ("1,2,4", 256, "63960835bcdc130f0b66d7ff4f6a5a8e"),
    ],
    ids=[
        "''_should_be_a2582a3a0e66e6e86e3812dcb672a272",
        "AoC 2017_should_be_33efeb34ea91902bb2f59c9920caa6cd",
        "1,2,3_should_be_3efbe78a8d82f29979031a4aa0b16a9d",
        "1,2,4_should_be_63960835bcdc130f0b66d7ff4f6a5a8e",
    ],
)
def test_part1(input_: str, size: int, expected: str) -> None:
    result: str = solve(input_, size)
    assert result == expected, f"got {result}, needs {expected}"
