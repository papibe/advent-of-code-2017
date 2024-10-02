from collections import namedtuple
from typing import List, Set, Tuple

Node = namedtuple("Node", ["row", "col"])
Cluster = Set[Node]

INFECTED_NODE: str = "#"


class Carrier:
    def __init__(self, row: int, col: int) -> None:
        self.row: int = row
        self.col: int = col
        self.dir: Node = Node(-1, 0)

    def position(self) -> Node:
        return Node(self.row, self.col)

    def turn_right(self) -> None:
        self.dir = Node(self.dir.col, -self.dir.row)

    def turn_left(self) -> None:
        self.dir = Node(-self.dir.col, self.dir.row)

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


def solve(carrier: Carrier, cluster: Set[Node], bursts: int) -> int:
    infections: int = 0

    for _ in range(bursts):
        position: Node = carrier.position()

        # determine turn
        if position in cluster:
            carrier.turn_right()
        else:
            carrier.turn_left()

        # determine infect
        if position not in cluster:
            infections += 1
            cluster.add(carrier.position())
        else:
            cluster.remove(carrier.position())

        # actual move
        carrier.move()

    return infections


def solution(filename: str, bursts: int) -> int:
    cluster, nodes = parse(filename)
    return solve(cluster, nodes, bursts)


if __name__ == "__main__":
    print(solution("./input.txt", 10_000))  # 5575
