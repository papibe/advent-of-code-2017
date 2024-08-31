import pytest

from part1_v1 import NUM_PAIRS, solution


@pytest.mark.parametrize(
    "a_value,b_value,pairs,expected",
    [
        (65, 8921, 5, 1),
        (65, 8921, NUM_PAIRS, 588),
    ],
    ids=[
        "a_starts_with_65_b_starts_with_8921_5_pairs_should_be_1",
        "a_starts_with_65_b_starts_with_8921_40M_pairs_should_be_588",
    ],
)
def test_part1(a_value: int, b_value: int, pairs: int, expected: int) -> None:
    result: int = solution(a_value, b_value, pairs)
    assert result == expected, f"got {result}, needs {expected}"
