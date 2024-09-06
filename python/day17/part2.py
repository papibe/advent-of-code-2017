import re
from collections import deque
from typing import Deque, Dict, List, Match, Optional, Set, Tuple


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node = None
        self.prev: Node = None

class Buffer:
    def __init__(self, spinlock: int) -> None:
        node: Node = Node(0)
        node.next = node
        node.prev = node

        self.head: Node = node
        self.size: int = 1
        self.spinlock: int = spinlock
        self.zero: Node = node

    def insert(self, value: int) -> None:
        position: int = self.spinlock % self.size
        p: Node = self.head
        for _ in range(position):
            p = p.next

        node: Node = Node(value)
        next_: Node = p.next
        p.next = node
        node.prev = p
        node.next = next_
        next_.prev = node

        self.head = node
        self.size += 1

    def print(self) -> None:
        p: Node = self.zero
        for _ in range(self.size):
            if p == self.head:
                print(f"({p.value})", end=" ")
            else:
                print(p.value, end=" ")
            p = p.next

        print()


def solution(spinlock: int) -> int:
    buffer: Buffer = Buffer(spinlock)

    for value in range(1, 50000000 + 1):
    # for value in range(1, 10):
        buffer.insert(value)
        # buffer.print()

    return buffer.zero.next.value


if __name__ == "__main__":
    print(solution(371))  # 39170601
