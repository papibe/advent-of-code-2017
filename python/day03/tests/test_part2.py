import pytest

from part2 import solution


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (1, 1, 2),
        (2, 3, 4),
        (4, 4, 5),
        (5, 9, 10),
        (10, 10, 11),
        (11, 22, 23),
        (23, 24, 25),
        (25, 25, 26),
        (26, 53, 54),
        (54, 56, 57),
        (57, 58, 59),
        (59, 121, 122),
        (122, 132, 133),
        (133, 141, 142),
        (142, 146, 147),
        (147, 303, 304),
        (304, 329, 330),
        (330, 350, 351),
        (351, 361, 362),
        (362, 746, 747),
    ],
    ids=[
        "from_1_to_1_should_return_2",
        "from_2_to_3_should_return_4",
        "from_4_to_4_should_return_5",
        "from_5_to_9_should_return_10",
        "from_10_to_10_should_return_11",
        "from_11_to_22_should_return_23",
        "from_23_to_24_should_return_25",
        "from_25_to_25_should_return_26",
        "from_26_to_53_should_return_54",
        "from_54_to_56_should_return_57",
        "from_57_to_58_should_return_59",
        "from_59_to_121_should_return_122",
        "from_122_to_132_should_return_133",
        "from_133_to_141_should_return_142",
        "from_142_to_146_should_return_147",
        "from_147_to_303_should_return_304",
        "from_304_to_329_should_return_330",
        "from_330_to_350_should_return_351",
        "from_351_to_361_should_return_362",
        "from_362_to_746_should_return_747",
    ],
)
def test_part2(start: int, end: int, expected: int) -> None:
    for parameter in range(start, end + 1):
        result: int = solution(parameter)
        assert result == expected, f"got {result}, needs {expected}"
