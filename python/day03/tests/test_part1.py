import pytest

from part1 import solution


@pytest.mark.parametrize(
    "input,expected",
    [
        # initial
        (1, 0),
        # next square of size 3
        (2, 1),
        (3, 2),
        (4, 1),
        (5, 2),
        (6, 1),
        (7, 2),
        (8, 1),
        (9, 2),
        # next square of size 5
        (10, 3),
        (11, 2),
        (12, 3),
        (13, 4),
        (14, 3),
        (15, 2),
        (16, 3),
        (17, 4),
        (18, 3),
        (19, 2),
        (20, 3),
        (21, 4),
        (22, 3),
        (23, 2),
        (24, 3),
        (25, 4),
        (1024, 31),
    ],
    ids=[
        # initial
        "1_should_be_0",
        # next square of size 3
        "2_should_be_1",
        "3_should_be_2",
        "4_should_be_1",
        "5_should_be_2",
        "6_should_be_1",
        "7_should_be_2",
        "8_should_be_1",
        "9_should_be_2",
        # next square of size 5
        "10_should_be_3",
        "11_should_be_2",
        "12_should_be_3",
        "13_should_be_4",
        "14_should_be_3",
        "15_should_be_2",
        "16_should_be_3",
        "17_should_be_4",
        "18_should_be_3",
        "19_should_be_2",
        "20_should_be_3",
        "21_should_be_4",
        "22_should_be_3",
        "23_should_be_2",
        "24_should_be_3",
        "25_should_be_4",
        "1024_should_be_31",
    ],
)
def test_part1(input: int, expected: int) -> None:
    result: int = solution(input)
    assert result == expected, f"got {result}, needs {expected}"
