from math import sqrt, ceil
from typing import List


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    for line in data:
        pass

    return data


def solve(data: List[str]) -> int:
    total_sum: int = 0

    for row in data:
        pass

    return total_sum


def solution(n: int) -> int:
    if n == 1:
        return 0

    aprox_upper_limit = ceil(sqrt(n))

    size: int
    if aprox_upper_limit % 2 == 0:
        size = aprox_upper_limit + 1
    else:
        size = aprox_upper_limit

    corner: int = size * size

    iterator: int = (size + 1) // 2
    steps_to_border: int = iterator - 1
    perimeter: int = 2 * size + 2 * (size - 2)

    # number_on_range: int = perimeter - n + 1
    # distance_to_corner: int = number_on_range % (size - 1)
    # half_distance_of_side: int = size // 2
    # adjusted: int = number_on_range + half_distance_of_side
    # adjusted_distance: int = adjusted % (half_distance_of_side)

    bottom: int = corner - size // 2
    left: int = corner - 3*(size // 2)
    top: int = corner - 5*(size // 2)
    right: int = corner - 7*(size // 2)

    # print(f"{n = }, {bottom = }, {left = }, {top = }, {right = }")
    # print(f"{n = }, {size = }")

    extra_steps: int = min(
        abs(bottom - n),
        abs(left - n),
        abs(top - n),
        abs(right - n),
    )

    # print(n,steps_to_border + extra_steps)
    return steps_to_border + extra_steps


if __name__ == "__main__":

    # for n in range(2, 9 + 1):
    #     solution(n)

    # for n in range(10, 25 + 1):
    #     solution(n)

    print(solution(1))  # 1
    print(solution(12))  # 3
    print(solution(23))  # 2
    print(solution(1024))  # 31
    print(solution(277678))  #
