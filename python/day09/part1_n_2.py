from typing import List, Tuple


def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data[0]


def garbage(data: str, index: int) -> Tuple[int, int]:
    garbage: int = 0
    while True:
        if data[index] == "!":
            index += 2
        elif data[index] == ">":
            return index, garbage
        else:
            garbage += 1
            index += 1


def flat_parse(data: str) -> Tuple[int, int]:
    score: int = 0
    index: int = 0
    level: int = 0
    total_garbage: int = 0

    while index < len(data):
        if data[index] == "{":
            level += 1
        elif data[index] == "<":
            index, garbage = garbage(data, index + 1)
            total_garbage += garbage
        elif data[index] == "}":
            score += level
            level -= 1
        index += 1

    return score, total_garbage


def solution(filename: str) -> Tuple[int, int]:
    data: str = parse(filename)
    return flat_parse(data)


if __name__ == "__main__":
    # print(flat_parse("{}"))  # 1
    # print(flat_parse("{{{}}}"))  # 6
    # print(flat_parse("{{},{}}"))  # 5
    # print(flat_parse("{{{},{},{{}}}}"))  # 16
    # print(flat_parse("{<a>,<a>,<a>,<a>}"))  # 1
    # print(flat_parse("{{<ab>},{<ab>},{<ab>},{<ab>}}"))  # 9
    # print(flat_parse("{{<!!>},{<!!>},{<!!>},{<!!>}}"))  # 9
    # print(flat_parse("{{<a!>},{<a!>},{<a!>},{<ab>}}"))  # 3

    solution1, solution2 = solution("./input.txt")
    print(f"Part1: {solution1}")  #
    print(f"Part2: {solution2}")  #
