from collections import namedtuple
from typing import List, Set, Tuple

Node = namedtuple("Node", ["row", "col"])
Cluster = Set[Node]

INFECTED_NODE: str = "#"


class Carrier:
    def __init__(self, row: int, col: int) -> None:
        self.row: int = row
        self.col: int = col
        self.dir: Node = Node(-1, 0)  # -> 1, 1 -> (1, 0) -> (0, -1)

    def position(self) -> Node:
        return Node(self.row, self.col)

    def turn_right(self) -> None:
        self.dir = Node(self.dir.col, -self.dir.row)

    def turn_left(self) -> None:
        self.dir = Node(-self.dir.col, self.dir.row)

    def reverse(self) -> None:
        self.dir = Node(-self.dir.row, -self.dir.col)

    def move(self) -> None:
        self.row += self.dir.row
        self.col += self.dir.col


def parse(filename: str) -> Tuple[Carrier, Cluster]:
    with open(filename, "r") as file:
        data: List[str] = file.read().splitlines()

    cluster: Set[Node] = set()

    rows: int = len(data)
    cols: int = len(data[0])
    for row in range(rows):
        for col in range(cols):
            if data[row][col] == INFECTED_NODE:
                cluster.add(Node(row, col))

    carrier = Carrier(rows // 2, cols // 2)

    return carrier, cluster


def solve(current: Carrier, infected: Set[Node], bursts: int) -> int:
    infections: int = 0
    weakened: Set[Node] = set()
    flagged: Set[Node] = set()

    for _ in range(bursts):
        position = current.position()

        if position in weakened:
            weakened.remove(position)
            infected.add(position)

            infections += 1

        elif position in infected:
            current.turn_right()

            infected.remove(position)
            flagged.add(position)

        elif position in flagged:
            current.reverse()

            flagged.remove(position)

        else:
            current.turn_left()

            weakened.add(position)

        current.move()

    return infections


def solution(filename: str, bursts: int) -> int:
    carrier, nodes = parse(filename)
    return solve(carrier, nodes, bursts)


if __name__ == "__main__":
    # print(solution("./example.txt"))  # 2511944
    print(solution("./input.txt", 10_000_000))  # 2511991
