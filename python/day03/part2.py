from typing import Dict, Iterator, Tuple

Coord = Tuple[int, int]
Grid = Dict[Coord, int]

DIRECTIONS = ((0, 1), (-1, 0), (0, -1), (1, 0))


def next_position(row: int, col: int, size: int) -> Iterator[Coord]:
    index: int = 0
    steps: int = 1
    while True:
        for _ in range(2):
            for _ in range(steps):
                row += DIRECTIONS[index][0]
                col += DIRECTIONS[index][1]
                yield row, col
            index = (index + 1) % len(DIRECTIONS)
        steps += 1


def set_grid_value(grid: Grid, row: int, col: int) -> int:
    return (
        grid.get((row - 1, col - 1), 0)
        + grid.get((row - 1, col), 0)
        + grid.get((row - 1, col + 1), 0)
        + grid.get((row, col - 1), 0)
        + grid.get((row, col + 1), 0)
        + grid.get((row + 1, col - 1), 0)
        + grid.get((row + 1, col), 0)
        + grid.get((row + 1, col + 1), 0)
    )


def solution(n: int) -> int:
    grid: Grid = {}

    start_row: int = 0
    start_col: int = 0

    side_size: int = 1
    value: int = 1

    grid[(0, 0)] = value

    while True:
        side_size += 2

        for row, col in next_position(start_row, start_col, side_size):
            grid[(row, col)] = set_grid_value(grid, row, col)

            if grid[(row, col)] > n:
                return grid[(row, col)]


if __name__ == "__main__":

    # print(solution(277678)) # 279138
    assert solution(277678) == 279138
