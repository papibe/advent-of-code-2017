import pytest

from part1_n_2 import garbage


@pytest.mark.parametrize(
    "data,expected",
    [
        ("<>", 0),
        ("<random characters>", 17),
        ("<<<<>", 3),
        ("<{!>}>", 2),
        ("<!!>", 0),
        ("<!!!>>", 0),
        ('<{o"i!a,<{i<a>', 10),
    ],
)
def test_garbage_index(data: str, expected: bool) -> None:
    _, result = garbage(data, 1)
    assert result == expected, f"got {result}, needs {expected}"
