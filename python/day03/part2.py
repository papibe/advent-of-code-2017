from math import sqrt, ceil
from typing import Dict, List, Set, Tuple

def next_position(start_row: int, start_col: int, size: int):
    yield (start_row, start_col)

    print("up")
    for delta in range(1, size - 1):
        yield start_row - delta, start_col

    print("left")
    for delta in range(1, size):
        yield start_row - size + 2, start_col - delta

    print("down")
    for delta in range(1, size):
        yield start_row - size + 2 + delta, start_col - size + 1

    print("right")
    for delta in range(1, size):
        yield start_row + 1, start_col - size + 1 + delta

    print("done")


def solution(n: int) -> int:

    grid: Dict[Tuple[int, int], int] = {(0,0): 1}

    size: int = 1
    start_row: int = 0
    start_col: int = 1

    counter: int = 0

    while True:
        size += 2
        perimeter: int = 2 * size + 2 * (size - 2)

        for row, col in next_position(start_row, start_col, size):
            value: int = (
                grid.get((row - 1, col - 1), 0)
                + grid.get((row - 1, col), 0)
                + grid.get((row - 1, col + 1), 0)
                + grid.get((row, col - 1), 0)
                + grid.get((row, col + 1), 0)
                + grid.get((row + 1, col - 1), 0)
                + grid.get((row + 1, col), 0)
                + grid.get((row + 1, col + 1), 0)
            )
            if value > n:
                return value
            print((row, col), value)
            grid[(row, col)] = value

        print(f"end {size = }")
        start_row = row
        start_col = col + 1

    return 0


if __name__ == "__main__":

    print(solution(277678))

    # for n in range(10, 25 + 1):
    #     solution(n)

    # print(solution(1))  # 1
    # print(solution(12))  # 3
    # print(solution(23))  # 2
    # print(solution(1024))  # 31
    # print(solution(277678))  #
