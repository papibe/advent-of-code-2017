import pytest

from part1 import solution


@pytest.mark.parametrize(
    "nodes_file,bursts,expected",
    [
        ("example.txt", 7, 5),
        ("example.txt", 70, 41),
        ("example.txt", 10_000, 5587),
    ],
    ids=[
        "example_7_bursts_should_be_5",
        "example_70_bursts_should_be_41",
        "example_10_000_bursts_should_be_5587",
    ],
)
def test_solve(nodes_file: str, bursts: int, expected: int) -> None:
    result: int = solution(nodes_file, bursts)
    assert result == expected, f"got {result}, needs {expected}"
