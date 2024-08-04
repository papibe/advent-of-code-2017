import re
from collections import deque
from typing import List


class Node:
    def __init__(
        self,
        value: int,
        index: int = 0,
        next_: "Node" = None,
        prev: "Node" = None,
    ) -> None:
        self.value = value
        self.index = index
        self.next = next_
        self.prev = prev

    def __repr__(self) -> str:
        return f"{self.value}"


class Elements:
    def __init__(self, size: int) -> None:
        self.size = size
        self.skip_size = 0
        self.current_postion = Node(value=0, index=0)
        self.head = self.current_postion
        prev = self.current_postion

        for value in range(1, self.size):
            n: Node = Node(value, index=value, next_=None, prev=prev)
            prev.next = n
            prev = n
        prev.next = self.current_postion
        self.current_postion.prev = prev

    def apply(self, length: int) -> None:

        head: Node = self.current_postion

        current: Node = self.current_postion
        for i in range(length - 1):
            current = current.next

        tail: Node = current

        while head != tail and head.prev != tail:
            value: int = head.value
            index: int = head.index

            head.value = tail.value
            head.index = tail.index
            tail.value = value
            tail.index = index

            head = head.next
            tail = tail.prev

        current = self.current_postion
        for _ in range(length + self.skip_size):
            current = current.next

        self.current_postion = current
        self.skip_size += 1

    def print(self) -> None:
        output = []
        current = self.head
        for _ in range(self.size):
            if current == self.current_postion:
                output.append(f"[{current.value}]")
            else:
                output.append(f"{current.value}")
            current = current.next
        print(" ".join(output))

    def top(self) -> None:
        return self.head.value * self.head.next.value


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().strip()
    return [int(e.strip()) for e in data.split(",")]


def solve(elements: Elements, lengths: List[int]) -> int:
    for length in lengths:
        elements.apply(length)
    return elements.top()


def solution(filename: str, size: int) -> int:
    lengths: List[int] = parse(filename)
    elements = Elements(size)
    return solve(elements, lengths)


if __name__ == "__main__":
    print(solution("./example.txt", 5))  # 12
    print(solution("./input.txt", 256))  # 40132
