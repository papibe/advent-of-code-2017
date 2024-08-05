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

    def top(self) -> int:
        return self.head.value * self.head.next.value


def parse(filename: str) -> List[int]:
    with open(filename, "r") as fp:
        data: str = fp.read().strip()

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
