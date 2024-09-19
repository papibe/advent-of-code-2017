class Buffer:
    def __init__(self, spinlock: int) -> None:

        self.head_position: int = 0
        self.size: int = 1
        self.spinlock: int = spinlock
        self.zero_position: int = 0
        self.next_to_zero: int = 0

    def insert(self, value: int) -> None:
        insert_position: int = self.spinlock % self.size

        if insert_position == self.zero_position:
            self.next_to_zero = value
            self.zero_position = self.size

        elif insert_position < self.zero_position:
            self.zero_position -= insert_position

        elif insert_position > self.zero_position:
            self.zero_position += self.size - insert_position

        self.size += 1


def solution(spinlock: int) -> int:
    buffer: Buffer = Buffer(spinlock)

    for value in range(1, 50000000 + 1):
        buffer.insert(value)

    return buffer.next_to_zero


if __name__ == "__main__":
    # it takes 4 secs
    print(solution(371))  # 39170601
