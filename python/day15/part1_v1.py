GEN_A_FACTOR: int = 16807
GEN_B_FACTOR: int = 48271
DIVISOR: int = 2147483647
MASK: int = 0xFFFF

NUM_PAIRS: int = 40_000_000


def generator(previous_value: int, factor: int) -> int:
    return (previous_value * factor) % DIVISOR


def solution(a_value: int, b_value: int, num_pairs: int) -> int:
    counter: int = 0

    for _ in range(num_pairs):
        a_value = generator(a_value, GEN_A_FACTOR)
        b_value = generator(b_value, GEN_B_FACTOR)

        if (a_value & MASK) == (b_value & MASK):
            counter += 1

    return counter


if __name__ == "__main__":
    print(solution(699, 124, NUM_PAIRS))  # 600
