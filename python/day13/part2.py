import re
from typing import Dict, List, Match, Optional, Set

Firewall = Dict[int, int]


def parse(filename: str) -> Firewall:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    regex: str = r"(?P<depth>\d+): (?P<range>\d+)"

    firewall: Firewall = {}

    for line in data:
        matches: Optional[Match[str]] = re.match(regex, line)
        assert matches is not None
        depth: int = int(matches.group("depth"))
        range_: int = int(matches.group("range"))
        firewall[depth] = range_

    return firewall


def is_at_top(picosecond: int, scanner_range: int) -> bool:
    return (picosecond % (2 * scanner_range - 2)) == 0


def pass_through_firewall(delay: int, firewall: Firewall) -> int:
    position: int = 0
    visited: Set[int] = set()

    while len(visited) < len(firewall):
        if position in firewall:
            depth: int = position
            range_: int = firewall[depth]
            if is_at_top(position + delay, range_):
                return False
            visited.add(depth)

        position += 1

    return True


def solve(firewall: Firewall) -> int:
    delay: int = 0
    while True:
        if pass_through_firewall(delay, firewall):
            return delay
        delay += 1


def solution(filename: str) -> int:
    firewall: Firewall = parse(filename)
    return solve(firewall)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 24
    print(solution("./input.txt"))  # 3966414
