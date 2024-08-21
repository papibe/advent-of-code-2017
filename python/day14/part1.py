from typing import List, Dict

ONES: Dict[str, int] = {
    "0": 0, # 0000
    "1": 1, # 0001
    "2": 1, # 0010
    "3": 2, # 0011
    "4": 1, # 0100
    "5": 2, # 0101
    "6": 2, # 0110
    "7": 3, # 0111
    "8": 1, # 1000
    "9": 2, # 1001
    "a": 2, # 1010
    "b": 3, # 1011
    "c": 2, # 1100
    "d": 3, # 1101
    "e": 3, # 1110
    "f": 4, # 1111
}


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


def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        data: str = fp.read().strip()

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
    for _ in range(16):
        xor: int = 0
        for _ in range(16):
            xor ^= current.value
            current = current.next
        dense_hash.append(xor)

    return "".join([f"{n:0{2}x}" for n in dense_hash])


def solution(input_: str, size: int) -> str:
    used_squares: int = 0
    for row_number in range(128):
        row_hash: str = solve(input_ + f"-{row_number}", size)
        for char in row_hash:
            used_squares += ONES[char]

    return used_squares


if __name__ == "__main__":
    print(solution("flqrgnkx", 256))  # 8108
    print(solution("hxtvlmkl", 256))  # 8214
