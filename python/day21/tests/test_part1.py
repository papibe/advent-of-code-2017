import pytest

from part1 import Art, Rules, INITIAL_ART, get_divisions


art2: Art = [
    "#..#",
    "....",
    "....",
    "#..#",
]

art3: Art = [
    "##.##.",
    "#..#..",
    "......",
    "##.##.",
    "#..#..",
    "......",
]


@pytest.mark.parametrize(
    "art,expected",
    [
        (INITIAL_ART, 1),

    ],
)
def test_3_divisions(art: Art, expected: int) -> None:
    result: int = len(get_divisions(art, 3))
    assert result == expected, f"got {result}, needs {expected}"

@pytest.mark.parametrize(
    "art,expected",
    [
        (art2, 4),
        (art3, 9)
    ],
)
def test_2_divisions(art: Art, expected: int) -> None:
    result: int = len(get_divisions(art, 2))
    assert result == expected, f"got {result}, needs {expected}"
