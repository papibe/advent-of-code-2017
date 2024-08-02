import re
from collections import deque
from typing import List

class Node:
    def __init__(self, value: int, next: "Node"=None, prev: "Node"=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f"{self.value}"

class Elements:
    def __init__(self, size: int) -> None:
        self.size = size
        self.skip_size = 0
        self.current_postion = Node(0)
        prev = self.current_postion

        for value in range(1, self.size):
            n: Node = Node(value, next=None, prev=prev)
            prev.next = n
            prev = n
        prev.next = self.current_postion
        self.current_postion.prev = prev



    def apply(self, length: int) -> None:
        head = self.current_postion.prev
        current = self.current_postion
        stack = []

        for _ in range(length):
            stack.append(current)
            current = current.next
        tail = current

        # print(head, tail, stack)

        # invert
        for index in range(len(stack) - 1):
            stack[index].prev = stack[index + 1]
            stack[index + 1].next = stack[index]

        tail.next = stack[-1]
        stack[-1].prev = tail

        head.prev = stack[0]
        stack[0].next = head






    def print(self) -> None:
        output = []
        start = self.current_postion
        current = start
        while current.next != start:
            output.append(str(current.value))
            current = current.next
        output.append(str(current.value))
        print(",".join(output))


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    for line in data:
        pass

    return data


def solve(elements: Elements, lengths : List[int]) -> int:
    for length in lengths:
        elements.print()
        elements.apply(length)
        elements.print()

def solution(lengths: str, size: int) -> int:
    elements = Elements(size)

    # output = []
    # start = elements.current_postion.prev
    # current = start
    # while current.prev != start:
    #     output.append(str(current.value))
    #     current = current.prev
    # output.append(str(current.value))
    # print(",".join(output))


    return solve(elements, lengths)


if __name__ == "__main__":
    print(solution([3, 4, 1, 5], 5))  # 0
    # print(solution([0, 1, 2, 3, 4], 256))  # 0

