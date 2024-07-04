from typing import List


def parse(filename: str) -> List[int]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return [int(n) for n in data]


def solve(instructions: List[int]) -> int:
    pointer: int = 0
    max_pointer: int = len(instructions) - 1
    steps: int = 1

    while True:
        jump: int = instructions[pointer]
        if jump >= 3:
            instructions[pointer] -= 1
        else:
            instructions[pointer] += 1

        pointer += jump
        if pointer > max_pointer or pointer < 0:
            return steps
        steps += 1


def solution(filename: str) -> int:
    instructions: List[int] = parse(filename)
    return solve(instructions)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 10
    print(solution("./input.txt"))  # 28178177
