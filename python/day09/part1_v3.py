import re
from collections import deque
from typing import List, Tuple


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data[0]

class Score:
    def __init__(self) -> None:
        self.score = 0
        self.garbage = 0

    def reset(self) -> None:
        self.score = 0
        self.garbage = 0

    def match(self, token: str, level: int) -> None:
        self.score += level

    def count(self) -> None:
        self.garbage += 1


score: Score = Score()


def garbage(data: str, index: int) -> int:
    while True:
        if data[index] == "!":
            index += 2
        elif data[index] == ">":
            return index + 1
        else:
            score.count()
            index += 1


def thing(data: str, index: int, level: int) -> int:
    if data[index] == '{':
        return group(data, index, level)
        # return thing(data, index, level)
    elif data[index] == "<":
        return garbage(data, index + 1)
    # elif data[index] == ",":
    #     print("wa")
    #     return thing(data, index + 1, level)
    elif data[index] == "}":
        print("oi")
        # score.match("group", level)

        return index
    else:
        print("ex ->", data[index], index, level)
        raise Exception("expecting { or <")


def group(data: str, index: int, level: int) -> int:
    if data[index] == '{':
        index = thing(data, index + 1, level + 1)
        if index > len(data) - 1:
            return index
        if data[index] == "}":
            score.match("group", level)
            index += 1
        elif data[index] == ",":
            print("->", data[index], index, level)
            index =  thing(data, index + 1, level + 1)
    else:
        print("ex ->", data[index], index, level)
        raise Exception("expecting {")

    if index > len(data) - 1:
        return index

    if data[index] == "}":
        score.match("group", level)
        return index + 1
    else:
        print("ex ->", data[index], index, level)

        raise Exception("expecting }")

def solve(data: str) -> int:
    score.reset()
    group(data, 0, 1)
    return score.score



def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solve("{}"))  # 1
    print(solve("{{{}}}"))  # 6
    print(solve("{{},{}}"))  # 5
    # print(solve("{{{},{},{{}}}}"))  # 16
    # print(solve("{<a>,<a>,<a>,<a>}"))  # 1
    # print(solve("{{<ab>},{<ab>},{<ab>},{<ab>}}"))  # 9
    # print(solve("{{<!!>},{<!!>},{<!!>},{<!!>}}"))  # 9
    # print(solve("{{<a!>},{<a!>},{<a!>},{<ab>}}"))  # 3

    # print(solution("./input.txt"))  #