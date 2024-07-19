import pytest

from part1 import collect_garbage


input_strings = [
    "<>",
    "<random characters>",
    "<<<<>",
    "<{!>}>",
    "<!!>",
    "<!!!>>",
    '<{o"i!a,<{i<a>',
]

input_data = [(s, len(s)) for s in input_strings]

@pytest.mark.parametrize(
    "data,expected",
    input_data
)
def test_part1_garbage(data: str, expected: bool) -> None:
    result: int = collect_garbage(data, 0)
    assert result == expected, f"got {result}, needs {expected}"
