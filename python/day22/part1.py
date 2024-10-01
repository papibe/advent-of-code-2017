from typing import List, Dict, Set, Tuple
from dataclasses import dataclass
from collections import namedtuple

Node = namedtuple("Node", ["row", "col"])
Grid = Set[Node]

RIGHT_ROT: Dict[Node, Node] = {
    Node(-1, 0): Node(0, 1),
    Node(0, 1): Node(1, 0),
    Node(1, 0): Node(0, -1),
    Node(0, -1): Node(-1, 0),
}

LEFT_ROT: Dict[Node, Node] = {
    Node(-1, 0): Node(0, -1),
    Node(0, -1): Node(1, 0),
    Node(1, 0): Node(0, 1),
    Node(0, 1): Node(-1, 0),
}


class Infected:
    def __init__(self, row: int, col: int) -> None:
        self.row: int = row
        self.col: int = col
        self.dir: Node = Node(-1, 0) # -> 1, 1 -> (1, 0) -> (0, -1)

    def position(self) -> Node:
        return Node(self.row, self.col)

    def turn_right(self) -> None:
        self.dir = RIGHT_ROT[self.dir]

    def turn_left(self) -> None:
        # print(self.dir)
        self.dir = LEFT_ROT[self.dir]
        # print(self.dir)

    def move(self) -> None:
        self.row += self.dir.row
        self.col += self.dir.col

    def __repr__(self) -> str:
        s: str = f"{self.row}, {self.col} -> {self.dir.row}, {self.dir.col}"
        return s

def parse(filename: str) -> Tuple[Infected, Grid]:
    with open(filename, "r") as file:
        data: List[str] = file.read().splitlines()

    nodes: Set[Node] = set()

    rows: int = len(data)
    cols: int = len(data[0])
    for row in range(rows):
        for col in range(cols):
            if data[row][col] == "#":
                nodes.add(Node(row, col))

    # print(nodes)
    current = Infected(rows // 2, cols // 2)

    return current, nodes    


def solve(current: Infected, nodes: Set[Node]) -> int:
    infections: int = 0

    # print(current)
    # print(nodes)
    # print()
    for _ in range(10_000):
        # turn
        if current.position() in nodes:
            # print("turn right")
            current.turn_right()
        else:
            # print("turn left")
            current.turn_left()

        # infect
        if current.position() not in nodes:
            infections += 1 
            # print("infect")
            nodes.add(current.position())
        else:
            # print("clean")
            nodes.remove(current.position())

        current.move()
        # print(current)
        # print(nodes)
        # print()

    return infections


def solution(filename: str) -> int:
    current, nodes = parse(filename)
    return solve(current, nodes)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 5587
    print(solution("./input.txt"))  # 5575