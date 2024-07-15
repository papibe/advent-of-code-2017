import re
from typing import Dict, List


def parse(filename: str) -> List[int]:
    with open(filename, "r") as fp:
        data_line: str = fp.read().splitlines()[0]

    return [int(n) for n in re.split("\s+", data_line)]


def hash_memory(instructions: List[int]) -> str:
    return ",".join([str(nblocks) for nblocks in instructions])


def reallocation(instructions: List[int]) -> None:
    # find max blocks
    max_blocks: int = float("-inf")  # type: ignore
    max_index: int = 0

    for bank_index, nblocks in enumerate(instructions):
        if nblocks > max_blocks:
            max_blocks = nblocks
            max_index = bank_index

    # redistribution process
    instructions[max_index] = 0
    index: int = (max_index + 1) % len(instructions)
    for _ in range(max_blocks):
        instructions[index] += 1
        index = (index + 1) % len(instructions)


def solve(instructions: List[int]) -> int:
    cycles: int = 0
    seen: Dict[str, int] = {}
    current_state: str = hash_memory(instructions)

    while current_state not in seen:
        seen[current_state] = cycles
        reallocation(instructions)
        current_state = hash_memory(instructions)
        cycles += 1

    return cycles - seen[current_state]


def solution(filename: str) -> int:
    data: List[int] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 4
    print(solution("./input.txt"))  # 2765
