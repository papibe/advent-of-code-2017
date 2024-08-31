GEN_A_FACTOR: int = 16807
GEN_B_FACTOR: int = 48271
DIVISOR: int = 2147483647
MASK: int = 0xFFFF

NUM_PAIRS: int = 5_000_000


class Generator:
    def __init__(self, initial_value: int, factor: int, multiple: int) -> None:
        self.value: int = initial_value
        self.factor: int = factor
        self.multiple: int = multiple

    def next(self) -> int:
        while True:
            self.value = (self.value * self.factor) % DIVISOR
            if (self.value % self.multiple) == 0:
                return self.value


def generator(previous_value: int, factor: int) -> int:
    return (previous_value * factor) % DIVISOR


def solve(gena: Generator, genb: Generator, num_pairs: int) -> int:
    counter: int = 0

    for _ in range(num_pairs):

        if (gena.next() & MASK) == (genb.next() & MASK):
            counter += 1

    return counter


def solution(previous_a_value: int, previous_b_value: int, num_pairs: int) -> int:
    generator_a: Generator = Generator(previous_a_value, GEN_A_FACTOR, 4)
    generator_b: Generator = Generator(previous_b_value, GEN_B_FACTOR, 8)
    return solve(generator_a, generator_b, num_pairs)


if __name__ == "__main__":
    print(solution(699, 124, NUM_PAIRS))  # 313
