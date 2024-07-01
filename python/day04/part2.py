from typing import List, Set


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data


def is_valid(line: str) -> int:
    words: List[str] = line.split(" ")
    number_of_words: int = len(words)

    sorted_words: Set[str] = set()
    for word in words:
        sorted_words.add("".join(sorted(word)))

    return number_of_words == len(sorted_words)


def solution(filename: str) -> int:
    data: List[str] = parse(filename)

    valid_passphrases: int = 0
    for line in data:
        if is_valid(line):
            valid_passphrases += 1

    return valid_passphrases


if __name__ == "__main__":
    print(solution("./input.txt"))  # 251
