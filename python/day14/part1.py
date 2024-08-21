from typing import Dict

import knot

ONES: Dict[str, int] = {
    "0": 0,  # 0000
    "1": 1,  # 0001
    "2": 1,  # 0010
    "3": 2,  # 0011
    "4": 1,  # 0100
    "5": 2,  # 0101
    "6": 2,  # 0110
    "7": 3,  # 0111
    "8": 1,  # 1000
    "9": 2,  # 1001
    "a": 2,  # 1010
    "b": 3,  # 1011
    "c": 2,  # 1100
    "d": 3,  # 1101
    "e": 3,  # 1110
    "f": 4,  # 1111
}


def solution(input_: str) -> int:
    used_squares: int = 0
    for row_number in range(128):
        row_hash: str = knot.hash(input_ + f"-{row_number}")
        for char in row_hash:
            used_squares += ONES[char]

    return used_squares


if __name__ == "__main__":
    print(solution("flqrgnkx"))  # 8108
    print(solution("hxtvlmkl"))  # 8214
