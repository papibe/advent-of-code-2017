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
        tail = self.current_postion.prev
        # print("tail", tail)
        current = self.current_postion
        next_ = current.next
        nnext = next_.next

        prev = current

        for i in range(length - 1):
            # print(f"{prev=}, {current=}, {next_=}, {nnext=}")

            current.prev = next_
            next_.next = current

            prev = current
            current = next_
            next_ = nnext
            nnext = nnext.next

            # next_ = current.next
            # next_next = next_.next
            # current.prev = next_
            # next_.next = current
            # prev = current
            # current = next_next.prev
            # print(f"   {prev=}, {current=}, {next_=}, {nnext=}\n")

        # current.prev = prev

        head = next_
        # print("head", head)

        tail.next = current
        current.prev = tail

        head.prev = self.current_postion
        self.current_postion.next = head

        self.current_postion = current
        print(f"starts at {current}")

        for _ in range(length + self.skip_size):
            current = current.next

        self.current_postion = current
        # print(f"    head: {self.current_postion}")
        self.skip_size += 1


    def print(self) -> None:
        output = []
        start = self.current_postion
        current = start
        while current.next != start:
            if current == self.current_postion:
                output.append(f"[{current.value}]")
            else:
                output.append(str(current.value))
            current = current.next
        output.append(str(current.value))
        print(" ".join(output))


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    for line in data:
        pass

    return data


def solve(elements: Elements, lengths : List[int]) -> int:
    for length in lengths:
        print(length)
        elements.print()
        elements.apply(length)
        print("    ", end="")
        elements.print()
    return 0

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

