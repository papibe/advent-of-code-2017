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


def solve(firewall: Firewall) -> int:
    severity: int = 0
    picosecond: int = 0  # also position
    visited: Set[int] = set()

    while len(visited) < len(firewall):
        if picosecond in firewall:
            depth: int = picosecond
            range_: int = firewall[depth]
            visited.add(depth)

            if is_at_top(picosecond, range_):
                severity += depth * range_

        picosecond += 1

    return severity


def solution(filename: str) -> int:
    firewall: Firewall = parse(filename)
    return solve(firewall)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 24
    print(solution("./input.txt"))  # 1900
