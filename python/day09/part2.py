from typing import List


def parse(filename: str) -> str:
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
        # print(token, level)
        if token == "group":
            self.score += level

    def count(self) -> None:
        self.garbage += 1


score: Score = Score()


def collect_garbage(data: str, index: int) -> int:
    while True:
        if data[index] == "!":
            index += 2
        elif data[index] == ">":
            score.match("garbage", 0)
            return index + 1
        else:
            score.count()
            index += 1


def thing(data: str, index: int, level: int) -> int:
    if data[index] == "{":
        return group(data, index, level)
    elif data[index] == "<":
        return collect_garbage(data, index + 1)
    elif data[index] == "}":
        # score.match("group", level)
        return index
    else:
        raise Exception("bla3")


def group(data: str, index: int, level: int) -> int:
    if data[index] == "{":
        while True:
            index = thing(data, index + 1, level + 1)
            if index > len(data) - 1:
                return index
            if data[index] == ",":
                # print(",")
                # index += 1
                continue
            else:
                break
    else:
        raise Exception("bla1")

    if index > len(data):
        return index

    if data[index] == "}":
        score.match("group", level)
        return index + 1
    else:
        raise Exception("bla2")


def solve(data: str) -> int:
    score.reset()
    group(data, 0, 1)
    return score.garbage


def solution(filename: str) -> int:
    data: str = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 7284
