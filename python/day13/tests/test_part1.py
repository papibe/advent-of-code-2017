import pytest

from part1 import is_at_top


@pytest.mark.parametrize(
    "index,size,expected",
    [
        # size 2
        (0, 2, True),
        (1, 2, False),
        (2, 2, True),
        (3, 2, False),
        (4, 2, True),
        (5, 2, False),
        (6, 2, True),
        (7, 2, False),
        (8, 2, True),
        (9, 2, False),
        # size 3
        (0, 3, True),
        (1, 3, False),
        (2, 3, False),
        (3, 3, False),
        (4, 3, True),
        (5, 3, False),
        (6, 3, False),
        (7, 3, False),
        (8, 3, True),
        (9, 3, False),
        # size 4
        (0, 4, True),
        (1, 4, False),
        (2, 4, False),
        (3, 4, False),
        (4, 4, False),
        (5, 4, False),
        (6, 4, True),
        (7, 4, False),
        (8, 4, False),
        (9, 4, False),
        # size 5
        (0, 5, True),
        (3, 5, False),
        (8, 5, True),
    ],
)
def test_part1(index: int, size: int, expected: int) -> None:
    result: int = is_at_top(index, size)
    assert result == expected, f"got {result}, needs {expected}"
