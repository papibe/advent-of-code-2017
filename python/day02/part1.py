import re
from typing import List

Spreadsheet = List[List[int]]


def parse(filename: str) -> Spreadsheet:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    spreadsheet: Spreadsheet = []

    for line in data:
        row: List[int] = [int(n) for n in re.split(r"\s", line)]
        spreadsheet.append(row)

    return spreadsheet


def solve(spreadsheet: Spreadsheet) -> int:
    checksum: int = 0

    for row in spreadsheet:
        min_value: int = min(row)
        max_value: int = max(row)
        checksum += max_value - min_value

    return checksum


def solution(filename: str) -> int:
    spreadsheet: Spreadsheet = parse(filename)
    return solve(spreadsheet)


if __name__ == "__main__":
    print(solution("./example1.txt"))  # 18
    print(solution("./input.txt"))  # 39126
