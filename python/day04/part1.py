from typing import List, Set


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data


def is_valid(line: str) -> int:
    words: List[str] = line.split(" ")
    number_of_words: int = len(words)
    unique_words: Set[str] = set(words)

    return number_of_words == len(unique_words)


def solution(filename: str) -> int:
    data: List[str] = parse(filename)

    valid_passphrases: int = 0
    for line in data:
        if is_valid(line):
            valid_passphrases += 1

    return valid_passphrases


if __name__ == "__main__":
    print(solution("./input.txt"))  # 466
