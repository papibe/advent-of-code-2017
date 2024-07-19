import re
from collections import deque
from typing import List, Tuple


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data[0]


def collect_garbage(data: str, index: int) -> int:
    while True:
        if data[index] == "!":
            index += 2
        elif data[index] == ">":
            return index + 1
        else:
            index += 1


def solve(data: str, start: int, end: int, level: int) -> int:
    score: int = 0
    internal_score: int = 0

    if start >= len(data):
        return 0, start

    if data[start] == "{":
        internal_score, next_index = solve(data, start + 1, end - 1, level + 1)
    elif data[start] == "}":
        score += 1
        internal_score, next_index = solve(data, start + 1, end - 1, level)
    elif data[start] == "<":
        next_index: int = collect_garbage(data, start + 1)
        internal_score, next_index = solve(data, next_index, end - 1, level + 1)

    c, i = solve(data, next_index, end, level)

    total = (score + c )* (level + 1) + internal_score * (level + 2), i
    print(f"{total = }")
    return total


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data, 0, len(data) - 1, 0)


if __name__ == "__main__":
    print(solve("{}", 0, 1,  0))  # 1
    print(solve("{{{}}}", 0, 5, 0))  # 6
    # print(solve("{{},{}}", 0, 1))  # 5
    # print(solve("{{{},{},{{}}}}", 0, 1))  # 16

    # print(solution("./input.txt"))  # 258
