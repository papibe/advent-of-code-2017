import pytest

from part1_n_2 import garbage


input_strings = [
    "<>",
    "<random characters>",
    "<<<<>",
    "<{!>}>",
    "<!!>",
    "<!!!>>",
    '<{o"i!a,<{i<a>',
]

input_data = [(s, len(s) - 1) for s in input_strings]

@pytest.mark.parametrize(
    "data,expected",
    input_data
)
def test_garbage_index(data: str, expected: bool) -> None:
    result, _ = garbage(data, 0)
    assert result == expected, f"got {result}, needs {expected}"
