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
        n: int = len(row)

        for i in range(n):
            for j in range(i + 1, n):
                if row[i] % row[j] == 0:
                    checksum += row[i] // row[j]
                elif row[j] % row[i] == 0:
                    checksum += row[j] // row[i]

    return checksum


def solution(filename: str) -> int:
    spreadsheet: Spreadsheet = parse(filename)
    return solve(spreadsheet)


if __name__ == "__main__":
    print(solution("./example2.txt"))  # 9
    print(solution("./input.txt"))  # 258
