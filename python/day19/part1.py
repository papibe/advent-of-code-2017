from typing import Generator, List, Tuple

Diagram = List[str]
Position = Tuple[int, int]

DIRECTIONS: List[Tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def parse(filename: str) -> Diagram:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data


def inbound(row: int, col: int, diagram: Diagram) -> bool:
    is_in_bound: bool = 0 <= row < len(diagram) and 0 <= col < len(diagram[0])
    return is_in_bound


def traverse(
    row: int, col: int, diagram: Diagram
) -> Generator[Position, Position, Position]:
    dir_row: int = 1
    dir_col: int = 0

    prev_row: int = row
    prev_col: int = col

    while diagram[row][col] != " ":

        if diagram[row][col] != "+":
            next_row: int = row + dir_row
            next_col: int = col + dir_col

            yield next_row, next_col
            prev_row, prev_col = row, col
            row, col = next_row, next_col
            continue

        # change direction
        for step_row, step_col in DIRECTIONS:
            neighbor_row: int = row + step_row
            neighbor_col: int = col + step_col

            if (
                (neighbor_row, neighbor_col) == (prev_row, prev_col)
                or not inbound(neighbor_row, neighbor_col, diagram)
                or diagram[neighbor_row][neighbor_col] == " "
            ):
                continue

            yield neighbor_row, neighbor_col
            dir_row = neighbor_row - next_row
            dir_col = neighbor_col - next_col

            prev_row, prev_col = row, col
            row, col = neighbor_row, neighbor_col

            break

    return row, col  # 'cause mypy non-sense


def solve(diagram: List[str]) -> str:
    path: List[str] = []

    # find start position
    start_col: int
    for start_col, char in enumerate(diagram[0]):
        if char != " ":
            break

    # traverse the diagram
    for row, col in traverse(0, start_col, diagram):
        current: str = diagram[row][col]
        if current.isalpha():
            path.append(current)

    return "".join(path)


def solution(filename: str) -> str:
    diagram: List[str] = parse(filename)
    return solve(diagram)


if __name__ == "__main__":
    print(solution("./example.txt"))  # "ABCDEF"
    print(solution("./input.txt"))  # "EOCZQMURF"
