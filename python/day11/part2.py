import re
from collections import deque
from typing import List
from collections import namedtuple
from typing import Dict

# Using hexagonal coordinates
# Souce: https://www.redblobgames.com/grids/hexagons/

HexCoord = namedtuple("HexCoord", ["q", "r", "s"])

DISTANCE: Dict[str, HexCoord] = {
    "n": HexCoord(0, 1, -1),
    "ne": HexCoord(1, 0, -1),
    "se": HexCoord(1, -1, 0),
    "s": HexCoord(0, -1, 1),
    "sw": HexCoord(-1, 0, 1),
    "nw": HexCoord(-1, 1, 0),
}


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data[0].split(",")


def solve(data: List[str]) -> int:
    current: HexCoord = HexCoord(0, 0, 0)
    max_distance: int = 0

    for dir in data:
        delta: HexCoord = DISTANCE[dir]
        current = HexCoord(
            current.q + delta.q,
            current.r + delta.r,
            current.s + delta.s,
        )
        max_distance: int = max(
            max_distance,
            max(abs(current.q), abs(current.r), abs(current.s)),
        )

    return max_distance


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 1469
