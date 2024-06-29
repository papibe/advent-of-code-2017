from math import ceil, sqrt
from typing import List


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()
    return data


def solution(n: int) -> int:
    aprox_box_size = ceil(sqrt(n))

    box_side: int = aprox_box_size + 1 if aprox_box_size % 2 == 0 else aprox_box_size
    lower_right_corner: int = box_side * box_side

    steps_to_border: int = (box_side + 1) // 2 - 1

    bottom: int = lower_right_corner - box_side // 2
    left: int = lower_right_corner - 3 * (box_side // 2)
    top: int = lower_right_corner - 5 * (box_side // 2)
    right: int = lower_right_corner - 7 * (box_side // 2)

    extra_steps: int = min(
        abs(bottom - n),
        abs(left - n),
        abs(top - n),
        abs(right - n),
    )
    return steps_to_border + extra_steps


if __name__ == "__main__":
    print(solution(277678))  # 475
