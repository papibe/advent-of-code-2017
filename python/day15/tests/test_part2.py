import pytest

from part2 import NUM_PAIRS, solution


@pytest.mark.parametrize(
    "a_value,b_value,pairs,expected",
    [
        (65, 8921, 5, 0),
        (65, 8921, 1056, 1),
        (65, 8921, NUM_PAIRS, 309),
    ],
    ids=[
        "a_starts_with_65_b_starts_with_8921_5_pairs_should_be_0",
        "a_starts_with_65_b_starts_with_8921_1056_pairs_should_be_1",
        "a_starts_with_65_b_starts_with_8921_5M_pairs_should_be_309",
    ],
)
def test_part1(a_value: int, b_value: int, pairs: int, expected: int) -> None:
    result: int = solution(a_value, b_value, pairs)
    assert result == expected, f"got {result}, needs {expected}"
