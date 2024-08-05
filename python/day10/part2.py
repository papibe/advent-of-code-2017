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


def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().strip()

    return data

def get_lengths(data: str) -> List[int]:
    final_sequence: List[int] = [ord(c) for c in data]
    final_sequence.extend([17, 31, 73, 47, 23])

    return final_sequence


def solve(input_: str, size: int) -> str:
    lengths: List[int] = get_lengths(input_)

    elements: Elements = Elements(size)

    for _ in range(64):
        for length in lengths:
            elements.apply(length)

    dense_hash: List[int] = []
    current: Node = elements.head
    for base in range(16):
        xor: int = 0
        for index in range(16):
            xor ^= current.value
            current = current.next
        dense_hash.append(xor)


    return "".join([f"{n:0{2}x}" for n in dense_hash])

def solution(filename: str, size: int) -> str:
    input_: str = parse(filename)
    # print(f"->{input_}<-")
    return solve(input_, size)


if __name__ == "__main__":
    assert solve("", 256) == "a2582a3a0e66e6e86e3812dcb672a272"
    assert solve("AoC 2017", 256) == "33efeb34ea91902bb2f59c9920caa6cd"
    assert solve("1,2,3", 256) == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert solve("1,2,4", 256) == "63960835bcdc130f0b66d7ff4f6a5a8e"

    print(solution("./input.txt", 256)) # "35b028fe2c958793f7d5a61d07a008c8"
