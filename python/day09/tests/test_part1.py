import pytest

from part1_n_2 import parse_stream


@pytest.mark.parametrize(
    "data,expected",
    [
        ("{}", 1),
        ("{{{}}}", 6),
        ("{{},{}}", 5),
        ("{{{},{},{{}}}}", 16),
        ("{<a>,<a>,<a>,<a>}", 1),
        ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
        ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
        ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
    ],
)
def test_part1(data: str, expected: bool) -> None:
    result, _ = parse_stream(data)
    assert result == expected, f"got {result}, needs {expected}"
