from typing import List, Tuple


def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data[0]


def garbage(data: str, index: int) -> Tuple[int, int]:
    garbage_counter: int = 0
    while True:
        if data[index] == "!":
            index += 2
        elif data[index] == ">":
            return index, garbage_counter
        else:
            garbage_counter += 1
            index += 1


def parse_stream(data: str) -> Tuple[int, int]:
    score: int = 0
    index: int = 0
    level: int = 0
    total_garbage: int = 0

    while index < len(data):
        if data[index] == "{":
            level += 1
        elif data[index] == "<":
            index, garbage_counter = garbage(data, index + 1)
            total_garbage += garbage_counter
        elif data[index] == "}":
            score += level
            level -= 1
        index += 1

    return score, total_garbage


def solution(filename: str) -> Tuple[int, int]:
    data: str = parse(filename)
    return parse_stream(data)


if __name__ == "__main__":
    solution1, solution2 = solution("./input.txt")
    print(f"Part1: {solution1}")  # 16869
    print(f"Part2: {solution2}")  # 7284
