from collections import deque
from typing import Deque, Dict, List, Set, Tuple

import knot

ONES: Dict[str, str] = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111",
}


def get_lengths(data: str) -> List[int]:
    final_sequence: List[int] = [ord(c) for c in data]
    final_sequence.extend([17, 31, 73, 47, 23])

    return final_sequence


def solution(input_: str) -> int:
    grid: List[str] = []
    for row_number in range(128):
        row_hash: str = knot.hash(input_ + f"-{row_number}")
        grid_row: List[str] = []

        for char in row_hash:
            grid_row.append(ONES[char])

        grid.append("".join(grid_row))

    regions: int = 0
    visited: Set[Tuple[int, int]] = set()

    for row in range(128):
        for col in range(128):
            if grid[row][col] == "0" or (row, col) in visited:
                continue

            # BFS
            regions += 1
            start = (row, col)
            visited.add(start)
            queue: Deque[Tuple[int, int]] = deque([start])

            while queue:
                current_row, current_col = queue.popleft()

                for step_row, step_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row: int = current_row + step_row
                    new_col: int = current_col + step_col

                    if 0 <= new_row < 128 and 0 <= new_col < 128:
                        if grid[new_row][new_col] == "0":
                            continue
                        if (new_row, new_col) not in visited:
                            queue.append((new_row, new_col))
                            visited.add((new_row, new_col))

    return regions


if __name__ == "__main__":
    print(solution("flqrgnkx"))  # 1242
    print(solution("hxtvlmkl"))  # 1093
