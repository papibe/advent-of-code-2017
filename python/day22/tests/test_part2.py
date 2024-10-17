import pytest

from part2 import solution


@pytest.mark.parametrize(
    "nodes_file,bursts,expected",
    [
        ("example.txt", 100, 26),
        ("example.txt", 10_000_000, 2511944),
    ],
    ids=[
        "example_100_bursts_should_be_26",
        "example_10_000_000_bursts_should_be_2511944",
    ],
)
def test_part1(nodes_file: str, bursts: int, expected: int) -> None:
    result: int = solution(nodes_file, bursts)
    assert result == expected, f"got {result}, needs {expected}"
