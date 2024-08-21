from typing import List


class Node:
    def __init__(
        self,
        value: int,
    ) -> None:
        self.value: int = value

    def set_next(self, next_: "Node") -> None:
        self.next: Node = next_

    def set_prev(self, prev: "Node") -> None:
        self.prev: Node = prev


class Elements:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.skip_size: int = 0
        self.current_postion: Node = Node(value=0)
        self.head: Node = self.current_postion
        prev = self.current_postion

        for value in range(1, self.size):
            n: Node = Node(value)
            n.set_prev(prev)
            prev.set_next(n)
            prev = n
        prev.set_next(self.current_postion)
        self.current_postion.set_prev(prev)

    def apply(self, length: int) -> None:

        current: Node = self.current_postion
        for _ in range(length - 1):
            current = current.next

        head: Node = self.current_postion
        tail: Node = current

        while head != tail and head.prev != tail:
            value: int = head.value

            head.value = tail.value
            tail.value = value

            head = head.next
            tail = tail.prev

        current = self.current_postion
        for _ in range(length + self.skip_size):
            current = current.next

        self.current_postion = current
        self.skip_size += 1


def get_lengths(data: str) -> List[int]:
    final_sequence: List[int] = [ord(c) for c in data]
    final_sequence.extend([17, 31, 73, 47, 23])

    return final_sequence


def hash(input_: str, size: int = 256) -> str:
    lengths: List[int] = get_lengths(input_)
    elements: Elements = Elements(size)

    for _ in range(64):
        for length in lengths:
            elements.apply(length)

    dense_hash: List[int] = []
    current: Node = elements.head
    for _ in range(16):
        xor: int = 0
        for _ in range(16):
            xor ^= current.value
            current = current.next
        dense_hash.append(xor)

    return "".join([f"{n:0{2}x}" for n in dense_hash])
